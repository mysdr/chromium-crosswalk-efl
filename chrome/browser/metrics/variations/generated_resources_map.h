// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CHROME_BROWSER_METRICS_VARIATIONS_GENERATED_RESOURCES_MAP_H_
#define CHROME_BROWSER_METRICS_VARIATIONS_GENERATED_RESOURCES_MAP_H_

#include "base/basictypes.h"

namespace chrome_variations {

// This file provides a mapping from hashes of generated resource names to their
// IDs. This mapping is achieved by having two arrays: |kResourceHashes|, a
// sorted array of resource name hashes; and |kResourceIndices|, an array of
// resource indices in the same order as |kResourceHashes|. So, if
// generated_resources.h contains |#define IDS_FOO 12345|, then for some index i
// kResourceHashes[i] = HASH("IDS_FOO") and kResourceIndices[i] = 12345. Both
// arrays are of length |kNumResources|.

// The definitions of the arrays are generated by generate_resources_map.py from
// the content of generated_resources.h.

// Length of |kResourceHashes| and |kResourceIndices|.
extern const size_t kNumResources;

// A sorted array of hashed generated resource names.
extern const uint32_t kResourceHashes[];

// An array of generated resource indices. The order of this array corresponds
// to the order of |kResourceHashes|.
extern const int kResourceIndices[];

// Gets the resource index corresponding to the given hash.
int GetResourceIndex(uint32_t hash);

}  // namespace chrome_variations

#endif  // CHROME_BROWSER_METRICS_VARIATIONS_GENERATED_RESOURCES_MAP_H_
