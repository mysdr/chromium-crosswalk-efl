// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef EXTENSIONS_BROWSER_UPDATER_MANIFEST_FETCH_DATA_H_
#define EXTENSIONS_BROWSER_UPDATER_MANIFEST_FETCH_DATA_H_

#include <map>
#include <set>
#include <string>

#include "base/basictypes.h"
#include "url/gurl.h"

namespace extensions {

// To save on server resources we can request updates for multiple extensions
// in one manifest check. This class helps us keep track of the id's for a
// given fetch, building up the actual URL, and what if anything to include
// in the ping parameter.
class ManifestFetchData {
 public:
  static const int kNeverPinged = -1;

  // What ping mode this fetch should use.
  enum PingMode {
    // No ping, no extra metrics.
    NO_PING,

    // Ping without extra metrics.
    PING,

    // Ping with extra metrics.
    PING_WITH_METRICS,
  };

  // Each ping type is sent at most once per day.
  enum PingType {
    // Used for counting total installs of an extension/app/theme.
    ROLLCALL,

    // Used for counting number of active users of an app, where "active" means
    // the app was launched at least once since the last active ping.
    ACTIVE,
  };

  struct PingData {
    // The number of days it's been since our last rollcall or active ping,
    // respectively. These are calculated based on the start of day from the
    // server's perspective.
    int rollcall_days;
    int active_days;
    // Wether the extension is enabled or not.
    bool is_enabled;

    PingData() : rollcall_days(0), active_days(0), is_enabled(true) {}
    PingData(int rollcall, int active, bool enabled)
        : rollcall_days(rollcall), active_days(active), is_enabled(enabled) {}
  };

  ManifestFetchData(const GURL& update_url,
                    int request_id,
                    const std::string& brand_code,
                    const std::string& base_query_params,
                    PingMode ping_mode);
  ~ManifestFetchData();

  // Returns true if this extension information was successfully added. If the
  // return value is false it means the full_url would have become too long, and
  // this ManifestFetchData object remains unchanged.
  bool AddExtension(const std::string& id,
                    const std::string& version,
                    const PingData* ping_data,
                    const std::string& update_url_data,
                    const std::string& install_source,
                    bool force_update);

  const GURL& base_url() const { return base_url_; }
  const GURL& full_url() const { return full_url_; }
  const std::set<std::string>& extension_ids() const { return extension_ids_; }
  const std::set<int>& request_ids() const { return request_ids_; }

  // Returns true if the given id is included in this manifest fetch.
  bool Includes(const std::string& extension_id) const;

  // Returns true if a ping parameter for |type| was added to full_url for this
  // extension id.
  bool DidPing(const std::string& extension_id, PingType type) const;

  // Assuming that both this ManifestFetchData and |other| have the same
  // full_url, this method merges the other information associated with the
  // fetch (in particular this adds all request ids associated with |other|
  // to this ManifestFetchData).
  void Merge(const ManifestFetchData& other);

  // Returns |true| if a given extension was forced to update.
  bool DidForceUpdate(const std::string& extension_id) const;

 private:
  // The set of extension id's for this ManifestFetchData.
  std::set<std::string> extension_ids_;

  // The set of ping data we actually sent.
  std::map<std::string, PingData> pings_;

  // The base update url without any arguments added.
  GURL base_url_;

  // The base update url plus arguments indicating the id, version, etc.
  // information about each extension.
  GURL full_url_;

  // The set of request ids associated with this manifest fetch. If multiple
  // requests are trying to fetch the same manifest, they can be merged into
  // one fetch, so potentially multiple request ids can get associated with
  // one ManifestFetchData.
  std::set<int> request_ids_;

  // The brand code to include with manifest fetch queries, if non-empty and
  // |ping_mode_| >= PING.
  const std::string brand_code_;

  // The ping mode for this fetch. This determines whether or not ping data
  // (and possibly extra metrics) will be included in the fetch query.
  const PingMode ping_mode_;

  // The set of extension IDs for which this fetch forced a CRX update.
  std::set<std::string> forced_updates_;

  DISALLOW_COPY_AND_ASSIGN(ManifestFetchData);
};

}  // namespace extensions

#endif  // EXTENSIONS_BROWSER_UPDATER_MANIFEST_FETCH_DATA_H_
