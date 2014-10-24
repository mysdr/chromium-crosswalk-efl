# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'layouttest_support_content_sources': [
      'public/test/layouttest_support.h',
      'public/test/nested_message_pump_android.cc',
      'public/test/nested_message_pump_android.h',
      'test/layouttest_support.cc',
      'test/test_media_stream_renderer_factory.cc',
      'test/test_media_stream_renderer_factory.h',
      'test/test_video_frame_provider.cc',
      'test/test_video_frame_provider.h',
    ],
    'test_support_content_sources': [
      'public/test/async_file_test_helper.cc',
      'public/test/async_file_test_helper.h',
      'public/test/browser_test_base.cc',
      'public/test/browser_test_base.h',
      'public/test/browser_test.h',
      'public/test/browser_test_utils.cc',
      'public/test/browser_test_utils.h',
      'public/test/content_test_suite_base.cc',
      'public/test/content_test_suite_base.h',
      'public/test/download_test_observer.cc',
      'public/test/download_test_observer.h',
      'public/test/fake_speech_recognition_manager.cc',
      'public/test/fake_speech_recognition_manager.h',
      'public/test/frame_load_waiter.cc',
      'public/test/frame_load_waiter.h',
      'public/test/javascript_test_observer.cc',
      'public/test/javascript_test_observer.h',
      'public/test/mock_blob_url_request_context.cc',
      'public/test/mock_blob_url_request_context.h',
      'public/test/mock_download_item.cc',
      'public/test/mock_download_item.h',
      'public/test/mock_download_manager.cc',
      'public/test/mock_download_manager.h',
      'public/test/mock_notification_observer.cc',
      'public/test/mock_notification_observer.h',
      'public/test/mock_render_process_host.cc',
      'public/test/mock_render_process_host.h',
      'public/test/mock_render_thread.cc',
      'public/test/mock_render_thread.h',
      'public/test/mock_resource_context.cc',
      'public/test/mock_resource_context.h',
      'public/test/mock_special_storage_policy.cc',
      'public/test/mock_special_storage_policy.h',
      'public/test/mock_storage_client.cc',
      'public/test/mock_storage_client.h',
      'public/test/render_view_test.cc',
      'public/test/render_view_test.h',
      'public/test/render_widget_test.cc',
      'public/test/render_widget_test.h',
      'public/test/sandbox_file_system_test_helper.cc',
      'public/test/sandbox_file_system_test_helper.h',
      'public/test/test_browser_context.cc',
      'public/test/test_browser_context.h',
      'public/test/test_browser_thread.cc',
      'public/test/test_browser_thread.h',
      'public/test/test_browser_thread_bundle.cc',
      'public/test/test_browser_thread_bundle.h',
      'public/test/test_content_client_initializer.cc',
      'public/test/test_content_client_initializer.h',
      'public/test/test_file_error_injector.cc',
      'public/test/test_file_error_injector.h',
      'public/test/test_file_system_backend.cc',
      'public/test/test_file_system_backend.h',
      'public/test/test_file_system_context.cc',
      'public/test/test_file_system_context.h',
      'public/test/test_file_system_options.cc',
      'public/test/test_file_system_options.h',
      'public/test/test_launcher.cc',
      'public/test/test_launcher.h',
      'public/test/test_navigation_observer.cc',
      'public/test/test_navigation_observer.h',
      'public/test/test_notification_tracker.cc',
      'public/test/test_notification_tracker.h',
      'public/test/test_renderer_host.cc',
      'public/test/test_renderer_host.h',
      'public/test/test_utils.cc',
      'public/test/test_utils.h',
      'public/test/unittest_test_suite.cc',
      'public/test/unittest_test_suite.h',
      'public/test/web_contents_tester.cc',
      'public/test/web_contents_tester.h',
      # TODO(phajdan.jr): All of those files should live in content/test (if
      # they're only used by content) or content/public/test (if they're used
      # by other embedders).
      'browser/download/mock_download_file.cc',
      'browser/download/mock_download_file.h',
      'browser/geolocation/fake_access_token_store.cc',
      'browser/geolocation/fake_access_token_store.h',
      'browser/geolocation/mock_location_arbitrator.cc',
      'browser/geolocation/mock_location_arbitrator.h',
      'browser/geolocation/mock_location_provider.cc',
      'browser/geolocation/mock_location_provider.h',
      'browser/renderer_host/media/mock_media_observer.cc',
      'browser/renderer_host/media/mock_media_observer.h',
      'browser/renderer_host/test/no_transport_image_transport_factory_android.cc',
      'browser/renderer_host/test/no_transport_image_transport_factory_android.h',
      'test/appcache_test_helper.cc',
      'test/appcache_test_helper.h',
      'test/blink_test_environment.cc',
      'test/blink_test_environment.h',
      'test/content_browser_test_utils_internal.cc',
      'test/content_browser_test_utils_internal.h',
      'test/content_test_suite.cc',
      'test/content_test_suite.h',
      'test/mock_google_streaming_server.cc',
      'test/mock_google_streaming_server.h',
      'test/mock_keyboard.cc',
      'test/mock_keyboard.h',
      'test/mock_keyboard_driver_win.cc',
      'test/mock_keyboard_driver_win.h',
      'test/mock_render_process.cc',
      'test/mock_render_process.h',
      'test/mock_webblob_registry_impl.cc',
      'test/mock_webblob_registry_impl.h',
      'test/mock_webclipboard_impl.cc',
      'test/mock_webclipboard_impl.h',
      'test/mock_webframeclient.h',
      'test/mock_weburlloader.cc',
      'test/mock_weburlloader.h',
      'test/net/url_request_abort_on_end_job.cc',
      'test/net/url_request_abort_on_end_job.h',
      'test/net/url_request_slow_download_job.cc',
      'test/net/url_request_slow_download_job.h',
      'test/ppapi_unittest.cc',
      'test/ppapi_unittest.h',
      'test/test_blink_web_unit_test_support.cc',
      'test/test_blink_web_unit_test_support.h',
      'test/test_content_browser_client.cc',
      'test/test_content_browser_client.h',
      'test/test_content_client.cc',
      'test/test_content_client.h',
      'test/test_frame_navigation_observer.cc',
      'test/test_frame_navigation_observer.h',
      'test/test_render_frame_host.cc',
      'test/test_render_frame_host.h',
      'test/test_render_frame_host_factory.cc',
      'test/test_render_frame_host_factory.h',
      'test/test_render_view_host.cc',
      'test/test_render_view_host.h',
      'test/test_render_view_host_factory.cc',
      'test/test_render_view_host_factory.h',
      'test/test_web_contents.cc',
      'test/test_web_contents.h',
      'test/web_gesture_curve_mock.cc',
      'test/web_gesture_curve_mock.h',
      'test/web_layer_tree_view_impl_for_testing.cc',
      'test/web_layer_tree_view_impl_for_testing.h',
      'test/weburl_loader_mock.cc',
      'test/weburl_loader_mock.h',
      'test/weburl_loader_mock_factory.cc',
      'test/weburl_loader_mock_factory.h',
    ]
  },
  'targets': [
    {
      # GN version: //content/test:layouttest_support
      'target_name': 'layouttest_support_content',
      'type': 'static_library',
      'conditions': [
        ['OS=="android"', {
          'dependencies': [
            'test_support_content_jni_headers',
          ],
        }],
        ['OS!="ios"', {
          # layouttest_support_content is not supported nor required on iOS.
          'dependencies': [
            'test_support_content',
            '../skia/skia.gyp:skia',
            '../ui/accessibility/accessibility.gyp:ax_gen',
            '../v8/tools/gyp/v8.gyp:v8',
          ],
          'include_dirs': [
            '..',
            '<(SHARED_INTERMEDIATE_DIR)',
          ],
          'sources': [ '<@(layouttest_support_content_sources)' ]
        }],
      ],
    },
    {
      # GN version: //content/test:test_support
      'target_name': 'test_support_content',
      'type': 'static_library',
      'dependencies': [
        '../net/net.gyp:net_test_support',
        '../skia/skia.gyp:skia',
        '../storage/storage_common.gyp:storage_common',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
        '../ui/accessibility/accessibility.gyp:ax_gen',
        '../ui/base/ui_base.gyp:ui_base',
        '../ui/base/ui_base.gyp:ui_base_test_support',
        '../ui/events/events.gyp:dom4_keycode_converter',
        '../ui/events/events.gyp:events_base',
        '../ui/events/events.gyp:events_test_support',
        '../ui/events/events.gyp:gesture_detection',
        '../ui/gfx/gfx.gyp:gfx_test_support',
        '../ui/resources/ui_resources.gyp:ui_resources',
        '../url/url.gyp:url_lib',
        'browser/speech/proto/speech_proto.gyp:speech_proto',
        'content.gyp:content_app_both',
        'content.gyp:content_browser',
        'content.gyp:content_common',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [ '<@(test_support_content_sources)' ],
      'conditions': [
        ['enable_plugins==0', {
          'sources!': [
            'test/ppapi_unittest.cc',
          ],
        }],
        ['enable_web_speech==0', {
          'sources!': [
            'test/mock_google_streaming_server.cc',
          ],
        }],
        ['OS == "ios"', {
          'sources/': [
            # iOS only needs a small portion of content; exclude all the
            # implementation, and re-include what is used.
            ['exclude', '\\.(cc|mm)$'],
            ['include', '_ios\\.(cc|mm)$'],
            ['include', '^public/test/content_test_suite_base\\.cc$'],
            ['include', '^public/test/mock_notification_observer\\.cc$'],
            ['include', '^public/test/mock_resource_context\\.cc$'],
            ['include', '^public/test/test_browser_thread\\.cc$'],
            ['include', '^public/test/test_content_client_initializer\\.cc$'],
            ['include', '^public/test/test_notification_tracker\\.cc$'],
            ['include', '^public/test/test_utils\\.cc$'],
            ['include', '^public/test/unittest_test_suite\\.cc$'],
            ['include', '^test/content_test_suite\\.cc$'],
            ['include', '^test/test_content_browser_client\\.cc$'],
            ['include', '^test/test_content_client\\.cc$'],
          ],
        }, {  # OS != "ios"
          'conditions': [
            ['OS=="mac"', {
              'copies': [{
                'destination': '<(SHARED_INTERMEDIATE_DIR)/webkit',
                'files': [
                  'shell/resources/missingImage.png',
                  'shell/resources/textAreaResizeCorner.png',
                ],
              }],
            }],
          ],
          'dependencies': [
            'content.gyp:content_child',
            'content.gyp:content_common',
            'content.gyp:content_gpu',
            'content.gyp:content_plugin',
            'content.gyp:content_ppapi_plugin',
            'content.gyp:content_renderer',
            'content.gyp:content_utility',
            'content_shell_and_tests.gyp:content_shell_pak',
            '../cc/blink/cc_blink.gyp:cc_blink',
            '../cc/cc.gyp:cc',
            '../cc/cc_tests.gyp:cc_test_support',
            '../media/blink/media_blink.gyp:media_blink',
            '../media/media.gyp:media',
            '../ppapi/ppapi_internal.gyp:ppapi_host',
            '../ppapi/ppapi_internal.gyp:ppapi_proxy',
            '../ppapi/ppapi_internal.gyp:ppapi_shared',
            '../ppapi/ppapi_internal.gyp:ppapi_unittest_shared',
            '../storage/storage_browser.gyp:storage',
            '../storage/storage_common.gyp:storage_common',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../ui/compositor/compositor.gyp:compositor_test_support',
            '../ui/surface/surface.gyp:surface',
            '../v8/tools/gyp/v8.gyp:v8',
            '../webkit/common/gpu/webkit_gpu.gyp:webkit_gpu',
          ],
          'export_dependent_settings': [
            '../third_party/WebKit/public/blink.gyp:blink',
          ],
        }],
        ['OS == "win"', {
          'dependencies': [
            '../sandbox/sandbox.gyp:sandbox',
            'content.gyp:content_startup_helper_win',
          ],
        }],
        ['enable_webrtc==1', {
          'sources': [
            'renderer/media/mock_media_stream_dispatcher.cc',
            'renderer/media/mock_media_stream_dispatcher.h',
            'renderer/media/mock_peer_connection_impl.cc',
            'renderer/media/mock_peer_connection_impl.h',
            'renderer/media/mock_web_rtc_peer_connection_handler_client.cc',
            'renderer/media/mock_web_rtc_peer_connection_handler_client.h',
            'renderer/media/webrtc/mock_peer_connection_dependency_factory.cc',
            'renderer/media/webrtc/mock_peer_connection_dependency_factory.h',
          ],
          'dependencies': [
            '../third_party/libjingle/libjingle.gyp:libjingle_webrtc',
            '../third_party/libjingle/libjingle.gyp:libpeerconnection',
            '../third_party/webrtc/modules/modules.gyp:video_capture_module',
          ],
        }],
        ['use_glib == 1', {
          'dependencies': [
            '../build/linux/system.gyp:glib',
          ],
        }],
        ['use_aura==1', {
          'dependencies': [
            '../ui/aura/aura.gyp:aura_test_support',
            '../ui/resources/ui_resources.gyp:ui_test_pak',
            '../ui/wm/wm.gyp:wm',
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            '../third_party/iaccessible2/iaccessible2.gyp:iaccessible2',
          ],
        }],
        ['OS!="android" and OS!="ios"', {
          'sources': [
            'browser/compositor/test/no_transport_image_transport_factory.cc',
            'browser/compositor/test/no_transport_image_transport_factory.h',
          ],
          'dependencies': [
            '../ui/compositor/compositor.gyp:compositor',
            '../third_party/libvpx/libvpx.gyp:libvpx',
          ],
        }],
        ['OS=="android"', {
          'dependencies': [
            '../ui/shell_dialogs/shell_dialogs.gyp:shell_dialogs',
          ],
        }],
      ],
    },
    {
      'target_name': 'content_unittests',
      'type': '<(gtest_target_type)',
      'dependencies': [
        'browser/service_worker/service_worker_proto.gyp:proto',
        'browser/speech/proto/speech_proto.gyp:speech_proto',
        'content.gyp:content_browser',
        'content.gyp:content_common',
        'test_support_content',
        '../base/base.gyp:test_support_base',
        '../crypto/crypto.gyp:crypto',
        '../net/net.gyp:net_test_support',
        '../skia/skia.gyp:skia',
        '../sql/sql.gyp:sql',
        '../sql/sql.gyp:test_support_sql',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
        '../third_party/re2/re2.gyp:re2',
        '../ui/accessibility/accessibility.gyp:accessibility',
        '../ui/base/ui_base.gyp:ui_base',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/gfx/gfx.gyp:gfx_geometry',
        '../ui/gfx/ipc/gfx_ipc.gyp:gfx_ipc',
      ],
      'include_dirs': [
        '..',
        '<(SHARED_INTERMEDIATE_DIR)',  # Needed by key_systems_unittest.cc.
      ],
      'sources': [
        'browser/accessibility/accessibility_mode_helper_unittest.cc',
        'browser/accessibility/browser_accessibility_mac_unittest.mm',
        'browser/accessibility/browser_accessibility_manager_unittest.cc',
        'browser/accessibility/browser_accessibility_win_unittest.cc',
        'browser/appcache/appcache_database_unittest.cc',
        'browser/appcache/appcache_disk_cache_unittest.cc',
        'browser/appcache/appcache_group_unittest.cc',
        'browser/appcache/appcache_host_unittest.cc',
        'browser/appcache/appcache_manifest_parser_unittest.cc',
        'browser/appcache/appcache_quota_client_unittest.cc',
        'browser/appcache/appcache_request_handler_unittest.cc',
        'browser/appcache/appcache_response_unittest.cc',
        'browser/appcache/appcache_service_unittest.cc',
        'browser/appcache/appcache_storage_unittest.cc',
        'browser/appcache/appcache_storage_impl_unittest.cc',
        'browser/appcache/appcache_unittest.cc',
        'browser/appcache/appcache_update_job_unittest.cc',
        'browser/appcache/appcache_url_request_job_unittest.cc',
        'browser/appcache/chrome_appcache_service_unittest.cc',
        'browser/appcache/mock_appcache_policy.cc',
        'browser/appcache/mock_appcache_policy.h',
        'browser/appcache/mock_appcache_service.cc',
        'browser/appcache/mock_appcache_service.h',
        'browser/appcache/mock_appcache_storage.cc',
        'browser/appcache/mock_appcache_storage.h',
        'browser/appcache/mock_appcache_storage_unittest.cc',
        'browser/battery_status/battery_status_manager_linux_unittest.cc',
        'browser/battery_status/battery_status_manager_win_unittest.cc',
        'browser/battery_status/battery_status_service_unittest.cc',
        'browser/browser_thread_unittest.cc',
        'browser/browser_url_handler_impl_unittest.cc',
        'browser/byte_stream_unittest.cc',
        'browser/child_process_security_policy_unittest.cc',
        'browser/cocoa/system_hotkey_map_unittest.mm',
        'browser/compositor/buffer_queue_unittest.cc',
        'browser/compositor/software_browser_compositor_output_surface_unittest.cc',
        'browser/compositor/software_output_device_ozone_unittest.cc',
        'browser/databases_table_unittest.cc',
        'browser/database_quota_client_unittest.cc',
        'browser/database_tracker_unittest.cc',
        'browser/database_util_unittest.cc',
        'browser/device_sensors/data_fetcher_shared_memory_base_unittest.cc',
        'browser/device_sensors/sensor_manager_android_unittest.cc',
        'browser/devtools/embedded_worker_devtools_manager_unittest.cc',
        'browser/devtools/devtools_http_handler_unittest.cc',
        'browser/devtools/devtools_manager_unittest.cc',
        'browser/dom_storage/dom_storage_area_unittest.cc',
        'browser/dom_storage/dom_storage_context_impl_unittest.cc',
        'browser/dom_storage/dom_storage_database_unittest.cc',
        'browser/dom_storage/session_storage_database_unittest.cc',
        'browser/download/base_file_unittest.cc',
        'browser/download/download_file_unittest.cc',
        'browser/download/download_item_impl_unittest.cc',
        'browser/download/download_manager_impl_unittest.cc',
        'browser/download/file_metadata_unittest_linux.cc',
        'browser/download/rate_estimator_unittest.cc',
        'browser/download/save_package_unittest.cc',
        'browser/fileapi/blob_storage_context_unittest.cc',
        'browser/fileapi/blob_url_request_job_unittest.cc',
        'browser/fileapi/copy_or_move_file_validator_unittest.cc',
        'browser/fileapi/copy_or_move_operation_delegate_unittest.cc',
        'browser/fileapi/dragged_file_util_unittest.cc',
        'browser/fileapi/external_mount_points_unittest.cc',
        'browser/fileapi/file_system_context_unittest.cc',
        'browser/fileapi/file_system_dir_url_request_job_unittest.cc',
        'browser/fileapi/file_system_file_stream_reader_unittest.cc',
        'browser/fileapi/file_system_operation_impl_unittest.cc',
        'browser/fileapi/file_system_operation_impl_write_unittest.cc',
        'browser/fileapi/file_system_operation_runner_unittest.cc',
        'browser/fileapi/file_system_quota_client_unittest.cc',
        'browser/fileapi/file_system_url_request_job_unittest.cc',
        'browser/fileapi/file_system_url_unittest.cc',
        'browser/fileapi/file_system_usage_cache_unittest.cc',
        'browser/fileapi/file_writer_delegate_unittest.cc',
        'browser/fileapi/fileapi_message_filter_unittest.cc',
        'browser/fileapi/isolated_context_unittest.cc',
        'browser/fileapi/local_file_stream_reader_unittest.cc',
        'browser/fileapi/local_file_stream_writer_unittest.cc',
        'browser/fileapi/local_file_util_unittest.cc',
        'browser/fileapi/mock_file_change_observer.cc',
        'browser/fileapi/mock_file_change_observer.h',
        'browser/fileapi/mock_file_update_observer.cc',
        'browser/fileapi/mock_file_update_observer.h',
        'browser/fileapi/mock_url_request_delegate.cc',
        'browser/fileapi/mock_url_request_delegate.h',
        'browser/fileapi/native_file_util_unittest.cc',
        'browser/fileapi/obfuscated_file_util_unittest.cc',
        'browser/fileapi/plugin_private_file_system_backend_unittest.cc',
        'browser/fileapi/recursive_operation_delegate_unittest.cc',
        'browser/fileapi/sandbox_database_test_helper.cc',
        'browser/fileapi/sandbox_database_test_helper.h',
        'browser/fileapi/sandbox_directory_database_unittest.cc',
        'browser/fileapi/sandbox_file_system_backend_delegate_unittest.cc',
        'browser/fileapi/sandbox_file_system_backend_unittest.cc',
        'browser/fileapi/sandbox_isolated_origin_database_unittest.cc',
        'browser/fileapi/sandbox_origin_database_unittest.cc',
        'browser/fileapi/sandbox_prioritized_origin_database_unittest.cc',
        'browser/fileapi/timed_task_helper_unittest.cc',
        'browser/fileapi/transient_file_util_unittest.cc',
        'browser/fileapi/upload_file_system_file_element_reader_unittest.cc',
        'browser/frame_host/frame_tree_unittest.cc',
        'browser/frame_host/navigation_controller_impl_unittest.cc',
        'browser/frame_host/navigation_entry_impl_unittest.cc',
        'browser/frame_host/navigator_impl_unittest.cc',
        'browser/frame_host/render_frame_host_manager_unittest.cc',
        'browser/frame_host/render_widget_host_view_child_frame_unittest.cc',
        'browser/frame_host/render_widget_host_view_guest_unittest.cc',
        'browser/gamepad/gamepad_provider_unittest.cc',
        'browser/gamepad/gamepad_service_unittest.cc',
        'browser/gamepad/gamepad_test_helpers.cc',
        'browser/gamepad/gamepad_test_helpers.h',
        'browser/geofencing/geofencing_manager_unittest.cc',
        'browser/geofencing/geofencing_service_unittest.cc',
        'browser/geolocation/geolocation_provider_impl_unittest.cc',
        'browser/geolocation/location_arbitrator_impl_unittest.cc',
        'browser/geolocation/network_location_provider_unittest.cc',
        'browser/geolocation/wifi_data_provider_chromeos_unittest.cc',
        'browser/geolocation/wifi_data_provider_common_unittest.cc',
        'browser/geolocation/wifi_data_provider_linux_unittest.cc',
        'browser/geolocation/wifi_data_provider_win_unittest.cc',
        'browser/gpu/gpu_data_manager_impl_private_unittest.cc',
        'browser/gpu/shader_disk_cache_unittest.cc',
        'browser/host_zoom_map_impl_unittest.cc',
        'browser/indexed_db/indexed_db_active_blob_registry_unittest.cc',
        'browser/indexed_db/indexed_db_backing_store_unittest.cc',
        'browser/indexed_db/indexed_db_cleanup_on_io_error_unittest.cc',
        'browser/indexed_db/indexed_db_database_unittest.cc',
        'browser/indexed_db/indexed_db_factory_unittest.cc',
        'browser/indexed_db/indexed_db_fake_backing_store.cc',
        'browser/indexed_db/indexed_db_fake_backing_store.h',
        'browser/indexed_db/indexed_db_leveldb_coding_unittest.cc',
        'browser/indexed_db/indexed_db_quota_client_unittest.cc',
        'browser/indexed_db/indexed_db_transaction_unittest.cc',
        'browser/indexed_db/indexed_db_unittest.cc',
        'browser/indexed_db/leveldb/mock_leveldb_factory.cc',
        'browser/indexed_db/leveldb/mock_leveldb_factory.h',
        'browser/indexed_db/mock_indexed_db_callbacks.cc',
        'browser/indexed_db/mock_indexed_db_callbacks.h',
        'browser/indexed_db/mock_indexed_db_database_callbacks.cc',
        'browser/indexed_db/mock_indexed_db_database_callbacks.h',
        'browser/indexed_db/mock_indexed_db_factory.cc',
        'browser/indexed_db/mock_indexed_db_factory.h',
        'browser/indexed_db/leveldb/leveldb_unittest.cc',
        'browser/indexed_db/list_set_unittest.cc',
        'browser/loader/resource_buffer_unittest.cc',
        'browser/loader/resource_dispatcher_host_unittest.cc',
        'browser/loader/resource_loader_unittest.cc',
        'browser/loader/resource_scheduler_unittest.cc',
        'browser/loader/temporary_file_stream_unittest.cc',
        'browser/loader/upload_data_stream_builder_unittest.cc',
        'browser/mach_broker_mac_unittest.cc',
        'browser/media/audio_stream_monitor_unittest.cc',
        'browser/media/capture/audio_mirroring_manager_unittest.cc',
        'browser/media/capture/video_capture_oracle_unittest.cc',
        'browser/media/capture/web_contents_audio_input_stream_unittest.cc',
        'browser/media/capture/web_contents_video_capture_device_unittest.cc',
        'browser/media/media_internals_unittest.cc',
        'browser/media/midi_host_unittest.cc',
        'browser/media/webrtc_identity_store_unittest.cc',
        'browser/net/sqlite_persistent_cookie_store_unittest.cc',
        'browser/notification_service_impl_unittest.cc',
        'browser/plugin_loader_posix_unittest.cc',
        'browser/power_monitor_message_broadcaster_unittest.cc',
        'browser/power_profiler/power_profiler_service_unittest.cc',
        'browser/quota/mock_quota_manager.cc',
        'browser/quota/mock_quota_manager.h',
        'browser/quota/mock_quota_manager_proxy.cc',
        'browser/quota/mock_quota_manager_proxy.h',
        'browser/quota/mock_quota_manager_unittest.cc',
        'browser/quota/quota_database_unittest.cc',
        'browser/quota/quota_backend_impl_unittest.cc',
        'browser/quota/quota_manager_unittest.cc',
        'browser/quota/quota_reservation_manager_unittest.cc',
        'browser/quota/quota_temporary_storage_evictor_unittest.cc',
        'browser/quota/storage_monitor_unittest.cc',
        'browser/quota/usage_tracker_unittest.cc',
        'browser/renderer_host/input/gesture_event_queue_unittest.cc',
        'browser/renderer_host/input/gesture_text_selector_unittest.cc',
        'browser/renderer_host/input/input_router_impl_unittest.cc',
        'browser/renderer_host/input/mock_input_ack_handler.cc',
        'browser/renderer_host/input/mock_input_ack_handler.h',
        'browser/renderer_host/input/mock_input_router_client.cc',
        'browser/renderer_host/input/mock_input_router_client.h',
        'browser/renderer_host/input/synthetic_gesture_controller_unittest.cc',
        'browser/renderer_host/input/tap_suppression_controller_unittest.cc',
        'browser/renderer_host/input/touch_action_filter_unittest.cc',
        'browser/renderer_host/input/touch_emulator_unittest.cc',
        'browser/renderer_host/input/touch_event_queue_unittest.cc',
        'browser/renderer_host/input/touch_handle_unittest.cc',
        'browser/renderer_host/input/touch_selection_controller_unittest.cc',
        'browser/renderer_host/input/web_input_event_util_unittest.cc',
        'browser/renderer_host/media/audio_input_device_manager_unittest.cc',
        'browser/renderer_host/media/audio_renderer_host_unittest.cc',
        'browser/renderer_host/media/media_stream_dispatcher_host_unittest.cc',
        'browser/renderer_host/media/media_stream_manager_unittest.cc',
        'browser/renderer_host/media/media_stream_ui_proxy_unittest.cc',
        'browser/renderer_host/media/video_capture_buffer_pool_unittest.cc',
        'browser/renderer_host/media/video_capture_controller_unittest.cc',
        'browser/renderer_host/media/video_capture_host_unittest.cc',
        'browser/renderer_host/media/video_capture_manager_unittest.cc',
        'browser/renderer_host/pepper/browser_ppapi_host_test.cc',
        'browser/renderer_host/pepper/browser_ppapi_host_test.h',
        'browser/renderer_host/pepper/pepper_file_system_browser_host_unittest.cc',
        'browser/renderer_host/pepper/pepper_gamepad_host_unittest.cc',
        'browser/renderer_host/pepper/pepper_printing_host_unittest.cc',
        'browser/renderer_host/pepper/quota_reservation_unittest.cc',
        'browser/renderer_host/render_process_host_unittest.cc',
        'browser/renderer_host/render_view_host_unittest.cc',
        'browser/renderer_host/render_widget_host_unittest.cc',
        'browser/renderer_host/render_widget_host_view_aura_unittest.cc',
        'browser/renderer_host/render_widget_host_view_base_unittest.cc',
        'browser/renderer_host/render_widget_host_view_mac_editcommand_helper_unittest.mm',
        'browser/renderer_host/render_widget_host_view_mac_unittest.mm',
        'browser/renderer_host/software_frame_manager_unittest.cc',
        'browser/renderer_host/text_input_client_mac_unittest.mm',
        'browser/renderer_host/web_input_event_aura_unittest.cc',
        'browser/renderer_host/websocket_dispatcher_host_unittest.cc',
        'browser/resolve_proxy_msg_helper_unittest.cc',
        'browser/service_worker/embedded_worker_instance_unittest.cc',
        'browser/service_worker/embedded_worker_test_helper.cc',
        'browser/service_worker/embedded_worker_test_helper.h',
        'browser/service_worker/service_worker_cache_unittest.cc',
        'browser/service_worker/service_worker_cache_storage_manager_unittest.cc',
        'browser/service_worker/service_worker_context_unittest.cc',
        'browser/service_worker/service_worker_controllee_request_handler_unittest.cc',
        'browser/service_worker/service_worker_context_request_handler_unittest.cc',
        'browser/service_worker/service_worker_database_unittest.cc',
        'browser/service_worker/service_worker_dispatcher_host_unittest.cc',
        'browser/service_worker/service_worker_handle_unittest.cc',
        'browser/service_worker/service_worker_job_unittest.cc',
        'browser/service_worker/service_worker_process_manager_unittest.cc',
        'browser/service_worker/service_worker_provider_host_unittest.cc',
        'browser/service_worker/service_worker_registration_unittest.cc',
        'browser/service_worker/service_worker_request_handler_unittest.cc',
        'browser/service_worker/service_worker_storage_unittest.cc',
        'browser/service_worker/service_worker_url_request_job_unittest.cc',
        'browser/service_worker/service_worker_utils_unittest.cc',
        'browser/service_worker/service_worker_version_unittest.cc',
        'browser/service_worker/service_worker_write_to_cache_job_unittest.cc',
        'browser/shared_worker/shared_worker_instance_unittest.cc',
        'browser/shared_worker/shared_worker_service_impl_unittest.cc',
        'browser/site_instance_impl_unittest.cc',
        'browser/speech/chunked_byte_buffer_unittest.cc',
        'browser/speech/endpointer/endpointer_unittest.cc',
        'browser/speech/google_one_shot_remote_engine_unittest.cc',
        'browser/speech/google_streaming_remote_engine_unittest.cc',
        'browser/speech/speech_recognizer_impl_unittest.cc',
        'browser/startup_task_runner_unittest.cc',
        'browser/storage_partition_impl_map_unittest.cc',
        'browser/storage_partition_impl_unittest.cc',
        'browser/streams/stream_unittest.cc',
        'browser/streams/stream_url_request_job_unittest.cc',
        'browser/system_message_window_win_unittest.cc',
        'browser/transition_request_manager_unittest.cc',
        'browser/web_contents/aura/overscroll_navigation_overlay_unittest.cc',
        'browser/web_contents/aura/window_slider_unittest.cc',
        'browser/web_contents/web_contents_delegate_unittest.cc',
        'browser/web_contents/web_contents_impl_unittest.cc',
        'browser/web_contents/web_contents_user_data_unittest.cc',
        'browser/web_contents/web_contents_view_mac_unittest.mm',
        'browser/web_contents/web_drag_dest_mac_unittest.mm',
        'browser/web_contents/web_drag_source_mac_unittest.mm',
        'browser/webui/web_ui_data_source_unittest.cc',
        'browser/webui/web_ui_message_handler_unittest.cc',
        'child/blink_platform_impl_unittest.cc',
        'child/fileapi/webfilewriter_base_unittest.cc',
        'child/indexed_db/indexed_db_dispatcher_unittest.cc',
        'child/indexed_db/webidbcursor_impl_unittest.cc',
        'child/multipart_response_delegate_unittest.cc',
        'child/npapi/plugin_lib_unittest.cc',
        'child/power_monitor_broadcast_source_unittest.cc',
        'child/resource_dispatcher_unittest.cc',
        'child/simple_webmimeregistry_impl_unittest.cc',
        'child/site_isolation_policy_unittest.cc',
        'child/web_gesture_curve_impl_unittest.cc',
        'child/web_url_loader_impl_unittest.cc',
        'child/webcrypto/test/aes_cbc_unittest.cc',
        'child/webcrypto/test/aes_ctr_unittest.cc',
        'child/webcrypto/test/aes_gcm_unittest.cc',
        'child/webcrypto/test/aes_kw_unittest.cc',
        'child/webcrypto/test/hmac_unittest.cc',
        'child/webcrypto/test/rsa_oaep_unittest.cc',
        'child/webcrypto/test/rsa_pss_unittest.cc',
        'child/webcrypto/test/rsa_ssa_unittest.cc',
        'child/webcrypto/test/sha_unittest.cc',
        'child/webcrypto/test/status_unittest.cc',
        'child/webcrypto/test/test_helpers.cc',
        'child/webcrypto/test/test_helpers.h',
        'child/worker_task_runner_unittest.cc',
        'common/android/address_parser_unittest.cc',
        'common/android/gin_java_bridge_value_unittest.cc',
        'common/cc_messages_unittest.cc',
        'common/common_param_traits_unittest.cc',
        'common/cursors/webcursor_unittest.cc',
        'common/database_connections_unittest.cc',
        'common/database_identifier_unittest.cc',
        'common/dom_storage/dom_storage_map_unittest.cc',
        'common/fileapi/file_system_util_unittest.cc',
        'common/gpu/gpu_memory_manager_unittest.cc',
        'common/host_shared_bitmap_manager_unittest.cc',
        'common/indexed_db/indexed_db_key_unittest.cc',
        'common/input/gesture_event_stream_validator_unittest.cc',
        'common/input/input_param_traits_unittest.cc',
        'common/input/touch_event_stream_validator_unittest.cc',
        'common/input/web_input_event_traits_unittest.cc',
        'common/inter_process_time_ticks_converter_unittest.cc',
        'common/mac/attributed_string_coder_unittest.mm',
        'common/mac/font_descriptor_unittest.mm',
        'common/one_writer_seqlock_unittest.cc',
        'common/page_state_serialization_unittest.cc',
        'common/page_zoom_unittest.cc',
        'common/plugin_list_unittest.cc',
        'common/sandbox_mac_diraccess_unittest.mm',
        'common/sandbox_mac_fontloading_unittest.mm',
        'common/sandbox_mac_system_access_unittest.mm',
        'common/sandbox_mac_unittest_helper.h',
        'common/sandbox_mac_unittest_helper.mm',
        'common/shareable_file_reference_unittest.cc',
        'common/webplugininfo_unittest.cc',
        'renderer/active_notification_tracker_unittest.cc',
        'renderer/android/email_detector_unittest.cc',
        'renderer/android/phone_number_detector_unittest.cc',
        'renderer/battery_status/battery_status_dispatcher_unittest.cc',
        'renderer/bmp_image_decoder_unittest.cc',
        'renderer/device_sensors/device_light_event_pump_unittest.cc',
        'renderer/device_sensors/device_motion_event_pump_unittest.cc',
        'renderer/device_sensors/device_orientation_event_pump_unittest.cc',
        'renderer/disambiguation_popup_helper_unittest.cc',
        'renderer/dom_storage/dom_storage_cached_area_unittest.cc',
        'renderer/gpu/frame_swap_message_queue_unittest.cc',
        'renderer/gpu/queue_message_swap_promise_unittest.cc',
        'renderer/gpu/render_widget_compositor_unittest.cc',
        'renderer/ico_image_decoder_unittest.cc',
        'renderer/input/input_event_filter_unittest.cc',
        'renderer/input/input_handler_proxy_unittest.cc',
        'renderer/manifest/manifest_parser_unittest.cc',
        'renderer/media/android/media_info_loader_unittest.cc',
        'renderer/media/audio_message_filter_unittest.cc',
        'renderer/media/audio_renderer_mixer_manager_unittest.cc',
        'renderer/media/crypto/key_systems_unittest.cc',
        'renderer/media/render_media_log_unittest.cc',
        'renderer/media/video_capture_impl_manager_unittest.cc',
        'renderer/media/video_capture_impl_unittest.cc',
        'renderer/media/video_capture_message_filter_unittest.cc',
        'renderer/media/webrtc/video_destination_handler_unittest.cc',
        'renderer/npapi/webplugin_impl_unittest.cc',
        'renderer/pepper/event_conversion_unittest.cc',
        'renderer/pepper/host_var_tracker_unittest.cc',
        'renderer/pepper/mock_resource.h',
        'renderer/pepper/pepper_broker_unittest.cc',
        'renderer/pepper/v8_var_converter_unittest.cc',
        'renderer/render_thread_impl_unittest.cc',
        'renderer/render_widget_unittest.cc',
        'renderer/scheduler/task_queue_manager_unittest.cc',
        'renderer/screen_orientation/screen_orientation_dispatcher_unittest.cc',
        'renderer/skia_benchmarking_extension_unittest.cc',
        'renderer/v8_value_converter_impl_unittest.cc',
        'test/fileapi_test_file_set.cc',
        'test/fileapi_test_file_set.h',
        'test/image_decoder_test.cc',
        'test/image_decoder_test.h',
        'test/run_all_unittests.cc',
      ],
      'conditions': [
        ['OS == "ios"', {
          'sources/': [
            # iOS only needs a small portion of content; exclude all the
            # implementation, and re-include what is used.
            ['exclude', '\\.(cc|mm)$'],
            ['include', '_ios\\.(cc|mm)$'],
            ['include', '^browser/notification_service_impl_unittest\\.cc$'],
            ['include', '^browser/web_contents/navigation_entry_impl_unittest\\.cc$'],
            ['include', '^test/run_all_unittests\\.cc$'],
          ],
        }, {  # OS != "ios"
          'dependencies': [
            'content.gyp:content_browser',
            'content.gyp:content_child',
            'content.gyp:content_gpu',
            'content.gyp:content_plugin',
            'content.gyp:content_renderer',
            'content.gyp:content_resources',
            '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
            '../cc/cc.gyp:cc',
            '../cc/cc.gyp:cc_surfaces',
            '../cc/cc_tests.gyp:cc_test_support',
            '../gin/gin.gyp:gin',
            '../gpu/gpu.gyp:gpu',
            '../gpu/gpu.gyp:gpu_unittest_utils',
            '../ipc/ipc.gyp:test_support_ipc',
            '../media/media.gyp:media_test_support',
            '../media/media.gyp:shared_memory_support',
            '../storage/storage_browser.gyp:storage',
            '../storage/storage_common.gyp:storage_common',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../third_party/icu/icu.gyp:icui18n',
            '../third_party/icu/icu.gyp:icuuc',
            '../third_party/leveldatabase/leveldatabase.gyp:leveldatabase',
            '../third_party/libjingle/libjingle.gyp:libjingle',
            '../ui/gl/gl.gyp:gl',
          ],
        }],
        ['OS != "win"', {
          'sources': [
            'browser/file_descriptor_info_impl_unittest.cc',
          ],
        }],
        ['enable_plugins==0', {
          'sources/': [
            ['exclude', '^browser/renderer_host/pepper/'],
            ['exclude', '^child/npapi/'],
            ['exclude', '^renderer/npapi/'],
            ['exclude', '^renderer/pepper/'],
          ],
          'sources!': [
            'browser/plugin_loader_posix_unittest.cc',
            'renderer/media/webrtc/video_destination_handler_unittest.cc',
          ],
        }],
        ['enable_webrtc==1', {
          'sources': [
            'browser/media/webrtc_internals_unittest.cc',
            'browser/renderer_host/media/webrtc_identity_service_host_unittest.cc',
            'browser/renderer_host/p2p/socket_host_test_utils.cc',
            'browser/renderer_host/p2p/socket_host_test_utils.h',
            'browser/renderer_host/p2p/socket_host_tcp_unittest.cc',
            'browser/renderer_host/p2p/socket_host_tcp_server_unittest.cc',
            'browser/renderer_host/p2p/socket_host_udp_unittest.cc',
            'browser/renderer_host/p2p/socket_host_unittest.cc',
            'renderer/media/media_stream_audio_processor_unittest.cc',
            'renderer/media/media_stream_constraints_util_unittest.cc',
            'renderer/media/media_stream_dispatcher_unittest.cc',
            'renderer/media/media_stream_video_capture_source_unittest.cc',
            'renderer/media/media_stream_video_source_unittest.cc',
            'renderer/media/media_stream_video_track_unittest.cc',
            'renderer/media/mock_media_stream_registry.cc',
            'renderer/media/mock_media_stream_registry.h',
            'renderer/media/mock_media_stream_video_sink.cc',
            'renderer/media/mock_media_stream_video_sink.h',
            'renderer/media/mock_media_stream_video_source.cc',
            'renderer/media/mock_media_stream_video_source.h',
            'renderer/media/mock_media_constraint_factory.cc',
            'renderer/media/rtc_peer_connection_handler_unittest.cc',
            'renderer/media/rtc_video_decoder_unittest.cc',
            'renderer/media/speech_recognition_audio_sink_unittest.cc',
            'renderer/media/user_media_client_impl_unittest.cc',
            'renderer/media/video_source_handler_unittest.cc',
            'renderer/media/webrtc/media_stream_remote_video_source_unittest.cc',
            'renderer/media/webrtc/media_stream_track_metrics_unittest.cc',
            'renderer/media/webrtc/peer_connection_dependency_factory_unittest.cc',
            'renderer/media/webrtc/webrtc_local_audio_track_adapter_unittest.cc',
            'renderer/media/webrtc/webrtc_media_stream_adapter_unittest.cc',
            'renderer/media/webrtc/webrtc_video_capturer_adapter_unittest.cc',
            'renderer/media/webrtc_audio_capturer_unittest.cc',
            'renderer/media/webrtc_audio_renderer_unittest.cc',
            'renderer/media/webrtc_identity_service_unittest.cc',
            'renderer/media/webrtc_local_audio_source_provider_unittest.cc',
            'renderer/media/webrtc_local_audio_track_unittest.cc',
            'renderer/media/webrtc_uma_histograms_unittest.cc',
            'renderer/p2p/ipc_network_manager_unittest.cc',
          ],
          'dependencies': [
            '../third_party/libjingle/libjingle.gyp:libjingle_webrtc',
            '../third_party/libjingle/libjingle.gyp:libpeerconnection',
            '../third_party/webrtc/modules/modules.gyp:video_capture_module',
          ]
        }, {
          'sources!': [
            'renderer/media/webrtc/video_destination_handler_unittest.cc',
          ],
        }],
        ['enable_webrtc==1 and (OS=="linux" or OS=="mac" or OS=="win")', {
          'sources': [
            'browser/media/capture/desktop_capture_device_unittest.cc',
          ],
          'dependencies': [
            '../third_party/webrtc/modules/modules.gyp:desktop_capture',
          ],
        }],
        ['enable_webrtc==1 and OS=="mac"', {
          'variables': {
            'libpeer_target_type%': 'static_library',
          },
          'conditions': [
            ['libpeer_target_type!="static_library"', {
              'copies': [{
                'destination': '<(PRODUCT_DIR)/Libraries',
                'files': [
                  '<(PRODUCT_DIR)/libpeerconnection.so',
                ],
              }],
            }],
          ],
        }],
        ['enable_webrtc==1 and chromeos==1', {
          'sources': [
            'browser/media/capture/desktop_capture_device_aura_unittest.cc',
          ],
        }],
        # TODO(jrg): remove the OS=="android" section?
        # http://crbug.com/113172
        # Understand better how media_stream_ is tied into Chromium.
        ['enable_webrtc==0 and OS=="android"', {
          'sources/': [
            ['exclude', '^renderer/media/media_stream_'],
          ],
        }],
        ['enable_web_speech==0', {
          'sources/': [
            ['exclude', '^browser/speech/'],
          ]
        }],
        ['notifications==0', {
           'sources!': [
             'renderer/active_notification_tracker_unittest.cc',
           ],
        }],
        ['OS=="linux"', {
          'dependencies': [
            '../build/linux/system.gyp:dbus',
            '../dbus/dbus.gyp:dbus_test_support',
          ],
        }],
        ['OS=="win" and win_use_allocator_shim==1', {
          'dependencies': [
            '../base/allocator/allocator.gyp:allocator',
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            '../third_party/iaccessible2/iaccessible2.gyp:iaccessible2',
          ],
        }],
        ['OS=="mac"', {
          # These flags are needed to run the test on Mac.
          # Search for comments about "xcode_settings" in chrome_tests.gypi.
          'xcode_settings': {'OTHER_LDFLAGS': ['-Wl,-ObjC']},
        }],
        ['chromeos==1', {
          'dependencies': [
            '../chromeos/chromeos.gyp:chromeos',
          ],
          'sources/': [
            ['exclude', '^browser/battery_status/battery_status_manager_linux_unittest.cc'],
            ['exclude', '^browser/geolocation/wifi_data_provider_linux_unittest.cc'],
          ],
        }],
        ['use_aura==1', {
          'dependencies': [
            '../ui/aura/aura.gyp:aura',
            '../ui/wm/wm.gyp:wm',
          ]
        }],
        ['use_aura==1 or toolkit_views==1', {
          'dependencies': [
            '../ui/events/events.gyp:events_test_support',
          ],
        }],
        ['use_aura!=1 and OS!="mac"', {
          'sources/': [
            ['exclude', '^browser/compositor/'],
          ],
        }],
        ['OS == "android"', {
          'sources': [
            'browser/android/java/gin_java_method_invocation_helper_unittest.cc',
            'browser/android/java/java_type_unittest.cc',
            'browser/android/java/jni_helper_unittest.cc',
            'browser/android/system_ui_resource_manager_impl_unittest.cc',
            'browser/renderer_host/input/motion_event_android_unittest.cc',
            'renderer/java/gin_java_bridge_value_converter_unittest.cc',
          ],
          'sources!': [
            'browser/geolocation/network_location_provider_unittest.cc',
            'browser/geolocation/wifi_data_provider_chromeos_unittest.cc',
            'browser/geolocation/wifi_data_provider_common_unittest.cc',
            'browser/geolocation/wifi_data_provider_linux_unittest.cc',
          ],
        }],
        ['OS != "android" and OS != "ios"', {
          'dependencies': [
            '../third_party/libvpx/libvpx.gyp:libvpx',
          ],
        }],
        ['OS == "android"', {
          'dependencies': [
            '../testing/android/native_test.gyp:native_test_native_code',
          ],
        }],
        ['use_aura!=1 and OS!="android"', {
          'sources!': [
            'browser/renderer_host/input/tap_suppression_controller_unittest.cc',
          ],
        }],
        ['use_dbus==0', {
          'sources!': [
            'browser/battery_status/battery_status_manager_linux_unittest.cc',
            'browser/geolocation/wifi_data_provider_linux_unittest.cc',
          ],
        }],
        ['OS!="win" and OS!="mac"', {
          'sources!': [
            'common/plugin_list_unittest.cc',
          ],
        }],
        ['use_ozone==1', {
          'dependencies': [
            '../ui/ozone/ozone.gyp:ozone_base',
          ],
        }],
      ],
    },
  ],
  'conditions': [
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'content_browsertests_run',
          'type': 'none',
          'dependencies': [
            'content_browsertests',
          ],
          'includes': [
            '../build/isolate.gypi',
          ],
          'sources': [
            'content_browsertests.isolate',
          ],
        },
        {
          'target_name': 'content_unittests_run',
          'type': 'none',
          'dependencies': [
            'content_unittests',
          ],
          'includes': [
            '../build/isolate.gypi',
          ],
          'sources': [
            'content_unittests.isolate',
          ],
          'conditions': [
            ['use_x11==1', {
              'dependencies': [
                '../tools/xdisplaycheck/xdisplaycheck.gyp:xdisplaycheck',
              ],
            }],
          ],
        },
      ],
      'conditions': [
        ['archive_gpu_tests==1', {
          'targets': [
            {
              'target_name': 'content_gl_tests_run',
              'type': 'none',
              'dependencies': [
                'content_shell_and_tests.gyp:content_gl_tests',
              ],
              'includes': [
                '../build/isolate.gypi',
              ],
              'sources': [
                'content_gl_tests.isolate',
              ],
            },
          ],
        }],
      ],
    }],
    ['OS!="ios"', {
      'targets': [
        {
          'target_name': 'content_perftests',
          'type': '<(gtest_target_type)',
          'defines!': ['CONTENT_IMPLEMENTATION'],
          'dependencies': [
            'content.gyp:content_browser',
            'content.gyp:content_common',
            'test_support_content',
            '../base/base.gyp:test_support_base',
            '../cc/cc.gyp:cc',
            '../skia/skia.gyp:skia',
            '../testing/gtest.gyp:gtest',
            '../testing/perf/perf_test.gyp:*',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
          ],
          'include_dirs': [
            '..',
          ],
          'sources': [
            'browser/renderer_host/input/input_router_impl_perftest.cc',
            'common/cc_messages_perftest.cc',
            'test/run_all_perftests.cc',
          ],
          'conditions': [
            ['OS == "android"', {
              'dependencies': [
                '../testing/android/native_test.gyp:native_test_native_code',
              ],
            }],
          ],
        },
        {
          'target_name': 'content_browser_test_support',
          'type': 'static_library',
          'dependencies': [
            'content_shell_lib',
            '../skia/skia.gyp:skia',
            '../testing/gtest.gyp:gtest',
            '../ui/accessibility/accessibility.gyp:ax_gen',
          ],
          'sources': [
            'test/content_test_launcher.cc',
            'public/test/content_browser_test.cc',
            'public/test/content_browser_test.h',
            'public/test/content_browser_test_utils.cc',
            'public/test/content_browser_test_utils.h',
            'public/test/content_browser_test_utils_mac.mm',
          ],
          'include_dirs': [
            '<(SHARED_INTERMEDIATE_DIR)',
          ],
          'conditions': [
            ['OS=="android"', {
              'dependencies': [
                'content.gyp:content_app_both',
              ],
            }, {
              'dependencies': [
                'content.gyp:content_browser',
              ],
            }],
          ],
        },
        {
          'target_name': 'web_ui_test_mojo_bindings',
          'type': 'static_library',
          'dependencies': [
            '../mojo/public/mojo_public.gyp:mojo_cpp_bindings',
          ],
          'sources': [
            'test/data/web_ui_test_mojo_bindings.mojom',
          ],
          'includes': [ '../mojo/public/tools/bindings/mojom_bindings_generator.gypi' ],
          'export_dependent_settings': [
            '../mojo/public/mojo_public.gyp:mojo_cpp_bindings',
          ],
        },
        {
          'target_name': 'content_browsertests',
          'type': '<(gtest_target_type)',
          'dependencies': [
            'content.gyp:content_common',
            'content.gyp:content_gpu',
            'content.gyp:content_plugin',
            'content.gyp:content_renderer',
            'content.gyp:content_resources',
            'content_browser_test_support',
            'content_shell_lib',
            'content_shell_pak',
            'test_support_content',
            'web_ui_test_mojo_bindings',
            '../base/base.gyp:test_support_base',
            '../gin/gin.gyp:gin',
            '../gpu/gpu.gyp:gpu',
            '../ipc/ipc.gyp:test_support_ipc',
            '../media/media.gyp:media_test_support',
            '../media/media.gyp:shared_memory_support',
            '../mojo/edk/mojo_edk.gyp:mojo_common_test_support',
            '../mojo/edk/mojo_edk.gyp:mojo_system_impl',
            '../mojo/mojo_base.gyp:mojo_environment_chromium',
            '../mojo/public/mojo_public.gyp:mojo_cpp_bindings',
            '../mojo/public/mojo_public.gyp:mojo_js_bindings',
            '../net/net.gyp:net_test_support',
            '../ppapi/ppapi_internal.gyp:ppapi_host',
            '../ppapi/ppapi_internal.gyp:ppapi_ipc',
            '../ppapi/ppapi_internal.gyp:ppapi_proxy',
            '../ppapi/ppapi_internal.gyp:ppapi_shared',
            '../ppapi/ppapi_internal.gyp:ppapi_tests',
            '../ppapi/ppapi_internal.gyp:ppapi_unittest_shared',
            '../testing/gmock.gyp:gmock',
            '../testing/gtest.gyp:gtest',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../third_party/leveldatabase/leveldatabase.gyp:leveldatabase',
            '../third_party/mesa/mesa.gyp:osmesa',
            '../ui/accessibility/accessibility.gyp:accessibility',
            '../ui/base/ui_base.gyp:ui_base',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
            '../ui/gl/gl.gyp:gl',
            '../ui/resources/ui_resources.gyp:ui_resources',
            '../ui/shell_dialogs/shell_dialogs.gyp:shell_dialogs',
            '../ui/snapshot/snapshot.gyp:snapshot',
            '../ui/accessibility/accessibility.gyp:ax_gen',
          ],
          'include_dirs': [
            '..',
            '<(SHARED_INTERMEDIATE_DIR)',  # Needed by encrypted_media_browsertest.cc
          ],
          'includes': [
            'browser/gpu/test_support_gpu.gypi',
          ],
          'defines': [
            'HAS_OUT_OF_PROC_TEST_RUNNER',
          ],
          'sources': [
            'app/mojo/mojo_browsertest.cc',
            'browser/accessibility/accessibility_mode_browsertest.cc',
            'browser/accessibility/accessibility_win_browsertest.cc',
            'browser/accessibility/android_hit_testing_browsertest.cc',
            'browser/accessibility/cross_platform_accessibility_browsertest.cc',
            'browser/accessibility/dump_accessibility_tree_browsertest.cc',
            'browser/accessibility/site_per_process_accessibility_browsertest.cc',
            'browser/battery_status/battery_status_browsertest.cc',
            'browser/compositor/image_transport_factory_browsertest.cc',
            'browser/bookmarklet_browsertest.cc',
            'browser/child_process_launcher_browsertest.cc',
            'browser/child_process_security_policy_browsertest.cc',
            'browser/cross_site_transfer_browsertest.cc',
            'browser/database_browsertest.cc',
            'browser/device_sensors/device_inertial_sensor_browsertest.cc',
            'browser/devtools/renderer_overrides_handler_browsertest.cc',
            'browser/dom_storage/dom_storage_browsertest.cc',
            'browser/download/download_browsertest.cc',
            'browser/download/drag_download_file_browsertest.cc',
            'browser/download/mhtml_generation_browsertest.cc',
            'browser/download/save_package_browsertest.cc',
            'browser/fileapi/file_system_browsertest.cc',
            'browser/frame_host/frame_tree_browsertest.cc',
            'browser/frame_host/render_frame_host_manager_browsertest.cc',
            'browser/frame_host/navigation_controller_impl_browsertest.cc',
            'browser/gpu/compositor_util_browsertest.cc',
            'browser/gpu/gpu_ipc_browsertests.cc',
            'browser/indexed_db/indexed_db_browsertest.cc',
            'browser/indexed_db/mock_browsertest_indexed_db_class_factory.cc',
            'browser/indexed_db/mock_browsertest_indexed_db_class_factory.h',
            'browser/loader/resource_dispatcher_host_browsertest.cc',
            'browser/manifest/manifest_browsertest.cc',
            'browser/media/encrypted_media_browsertest.cc',
            'browser/media/media_browsertest.cc',
            'browser/media/media_browsertest.h',
            'browser/media/media_canplaytype_browsertest.cc',
            'browser/media/media_source_browsertest.cc',
            'browser/net_info_browsertest.cc',
            'browser/plugin_data_remover_impl_browsertest.cc',
            'browser/plugin_browsertest.cc',
            'browser/plugin_service_impl_browsertest.cc',
            'browser/renderer_host/input/touch_action_browsertest.cc',
            'browser/renderer_host/input/touch_input_browsertest.cc',
            'browser/renderer_host/render_process_host_browsertest.cc',
            'browser/renderer_host/render_view_host_browsertest.cc',
            'browser/renderer_host/render_widget_host_browsertest.cc',
            'browser/renderer_host/render_widget_host_view_browsertest.cc',
            'browser/screen_orientation/screen_orientation_browsertest.cc',
            'browser/security_exploit_browsertest.cc',
            'browser/service_worker/service_worker_browsertest.cc',
            'browser/session_history_browsertest.cc',
            'browser/shared_worker/worker_browsertest.cc',
            'browser/site_per_process_browsertest.h',
            'browser/site_per_process_browsertest.cc',
            'browser/speech/speech_recognition_browsertest.cc',
            'browser/tracing/tracing_controller_browsertest.cc',
            'browser/transition_browsertest.cc',
            'browser/web_contents/opened_by_dom_browsertest.cc',
            'browser/web_contents/touch_editable_impl_aura_browsertest.cc',
            'browser/web_contents/web_contents_impl_browsertest.cc',
            'browser/web_contents/web_contents_view_aura_browsertest.cc',
            'browser/webkit_browsertest.cc',
            'browser/webui/web_ui_mojo_browsertest.cc',
            'child/site_isolation_policy_browsertest.cc',
            'renderer/accessibility/renderer_accessibility_browsertest.cc',
            'renderer/browser_render_view_browsertest.cc',
            'renderer/dom_serializer_browsertest.cc',
            'renderer/gin_browsertest.cc',
            'renderer/mouse_lock_dispatcher_browsertest.cc',
            'renderer/pepper/fake_pepper_plugin_instance.cc',
            'renderer/pepper/mock_renderer_ppapi_host.cc',
            'renderer/pepper/pepper_device_enumeration_host_helper_unittest.cc',
            'renderer/pepper/pepper_file_chooser_host_unittest.cc',
            'renderer/pepper/pepper_graphics_2d_host_unittest.cc',
            'renderer/pepper/pepper_url_request_unittest.cc',
            'renderer/render_thread_impl_browsertest.cc',
            'renderer/render_view_browsertest.cc',
            'renderer/render_view_browsertest_mac.mm',
            'renderer/render_widget_browsertest.cc',
            'renderer/resource_fetcher_browsertest.cc',
            'renderer/savable_resources_browsertest.cc',
            'test/accessibility_browser_test_utils.cc',
            'test/accessibility_browser_test_utils.h',
            'test/browser_test_utils_browsertest.cc',
            'test/content_browser_test_test.cc',
            'test/ppapi/ppapi_browsertest.cc',
            'test/ppapi/ppapi_test.cc',
            'test/ppapi/ppapi_test.h',
            'test/webui_resource_browsertest.cc',
          ],
          'conditions': [
            ['chromeos==0', {
              'sources!': [
                'browser/web_contents/touch_editable_impl_aura_browsertest.cc',
              ],
            }],
            ['OS=="win"', {
              'resource_include_dirs': [
                '<(SHARED_INTERMEDIATE_DIR)/webkit',
              ],
              'sources': [
                'shell/app/resource.h',
                'shell/app/shell.rc',
                # TODO:  It would be nice to have these pulled in
                # automatically from direct_dependent_settings in
                # their various targets (net.gyp:net_resources, etc.),
                # but that causes errors in other targets when
                # resulting .res files get referenced multiple times.
                '<(SHARED_INTERMEDIATE_DIR)/blink/public/resources/blink_resources.rc',
                '<(SHARED_INTERMEDIATE_DIR)/content/app/strings/content_strings_en-US.rc',
                '<(SHARED_INTERMEDIATE_DIR)/net/net_resources.rc',
              ],
              'dependencies': [
                '<(DEPTH)/content/app/strings/content_strings.gyp:content_strings',
                '<(DEPTH)/net/net.gyp:net_resources',
                '<(DEPTH)/third_party/WebKit/public/blink_resources.gyp:blink_resources',
                '<(DEPTH)/third_party/iaccessible2/iaccessible2.gyp:iaccessible2',
                '<(DEPTH)/third_party/isimpledom/isimpledom.gyp:isimpledom',
              ],
              'configurations': {
                'Debug_Base': {
                  'msvs_settings': {
                    'VCLinkerTool': {
                      'LinkIncremental': '<(msvs_large_module_debug_link_mode)',
                    },
                  },
                },
              },
              # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
              'msvs_disabled_warnings': [ 4267, ],
            }],
            ['OS=="win" and win_use_allocator_shim==1', {
              'dependencies': [
                '../base/allocator/allocator.gyp:allocator',
              ],
            }],
            ['OS=="linux"', {
              'sources!': [
                'browser/accessibility/dump_accessibility_tree_browsertest.cc',
              ],
            }],
            ['OS!="android"', {
              'sources!': [
                'browser/accessibility/android_hit_testing_browsertest.cc',
              ]
            }],
            ['OS=="android"', {
              'sources': [
                'shell/android/browsertests_apk/content_browser_tests_android.cc',
              ],
              'dependencies': [
                'content_shell_jni_headers',
                'content_shell_lib',
                '../testing/android/native_test.gyp:native_test_util',
              ],
            }],
            ['OS=="mac"', {
              'dependencies': [
                'content_shell',  # Needed for Content Shell.app's Helper.
              ],
              'sources': [
                'renderer/external_popup_menu_browsertest.cc',
              ],
            }],
            ['use_aura==1 and OS!="win"', {
              'sources!': [
                'browser/plugin_browsertest.cc',
              ],
            }],
            ['use_aura==1 or toolkit_views==1', {
              'dependencies': [
                '../ui/events/events.gyp:events_test_support',
              ],
            }],
            ['use_aura!=1 and OS!="mac"', {
              'sources/': [
                ['exclude', '^browser/compositor/'],
              ],
            }],
            ['OS!="android" and OS!="ios" and OS!="linux"', {
              # npapi test plugin doesn't build on android or ios
              'dependencies': [
                # Runtime dependencies
                'copy_npapi_test_plugin',
              ],
            }],
            ['enable_webrtc==1', {
              'sources': [
                'browser/media/webrtc_aecdump_browsertest.cc',
                'browser/media/webrtc_browsertest.cc',
                'browser/media/webrtc_getusermedia_browsertest.cc',
                'browser/media/webrtc_internals_browsertest.cc',
                'browser/media/webrtc_webcam_browsertest.cc',
                'test/webrtc_content_browsertest_base.cc',
                'test/webrtc_content_browsertest_base.h',
              ],
              'dependencies': [
                '../testing/perf/perf_test.gyp:perf_test',
              ],
            }],
            ['enable_plugins==0', {
              'sources/': [
                ['exclude', '^renderer/pepper/'],
              ],
              'sources!': [
                'browser/plugin_service_impl_browsertest.cc',
                'browser/plugin_data_remover_impl_browsertest.cc',
                'test/ppapi/ppapi_browsertest.cc',
                'test/ppapi/ppapi_test.cc',
                'test/ppapi/ppapi_test.h',
              ],
              'dependencies!': [
                '../ppapi/ppapi_internal.gyp:ppapi_tests',
              ]
            }],
            ['enable_web_speech==0', {
              'sources/': [
                ['exclude', '^browser/speech/'],
              ]
            }],
            ['branding=="Chrome"', {
              'sources!': [
                # These tests depend on single process mode, which is disabled
                # in official builds.
                'renderer/browser_render_view_browsertest.cc',
                'renderer/dom_serializer_browsertest.cc',
                'renderer/resource_fetcher_browsertest.cc',
                'renderer/savable_resources_browsertest.cc',
              ],
            }],
          ],
        },
        {
          'target_name': 'content_gl_tests',
          'type': '<(gtest_target_type)',
          'dependencies': [
            'content.gyp:content_common',
            'test_support_content',
            '../base/base.gyp:test_support_base',
            '../gpu/gpu.gyp:command_buffer_common',
            '../testing/gtest.gyp:gtest',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../ui/base/ui_base.gyp:ui_base',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
            '../ui/gfx/gfx.gyp:gfx_test_support',
            '../ui/gl/gl.gyp:gl',
            '../v8/tools/gyp/v8.gyp:v8',
          ],
          'include_dirs': [
            '..',
          ],
          'sources': [
            'common/gpu/client/gl_helper_unittest.cc',
            'common/gpu/client/gpu_in_process_context_tests.cc',
          ],
          'conditions': [
            ['OS=="android"', {
              'dependencies': [
                '../testing/android/native_test.gyp:native_test_native_code',
              ],
            }, {
              'dependencies': [
                # Runtime dependencis.
                '../third_party/ffmpeg/ffmpeg.gyp:ffmpeg',
                '../third_party/mesa/mesa.gyp:osmesa',
              ],
            }],
          ],
        },
        {
          'target_name': 'content_gl_benchmark',
          'type': '<(gtest_target_type)',
          'dependencies': [
            'content.gyp:content_common',
            'test_support_content',
            '../base/base.gyp:test_support_base',
            '../testing/gtest.gyp:gtest',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../ui/base/ui_base.gyp:ui_base',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
            '../ui/gl/gl.gyp:gl',
          ],
          'include_dirs': [
            '..',
          ],
          'sources': [
            'common/gpu/client/gl_helper_benchmark.cc',
          ],
        },
      ],
    }],
    ['(chromeos==1 or OS=="win" or OS=="android") and use_ozone==0', {
      'targets': [
          {
            'target_name': 'video_decode_accelerator_unittest',
            'type': '<(gtest_target_type)',
            'dependencies': [
              '../base/base.gyp:base',
              '../media/media.gyp:media',
              '../testing/gtest.gyp:gtest',
              '../ui/base/ui_base.gyp:ui_base',
              '../ui/gfx/gfx.gyp:gfx',
              '../ui/gfx/gfx.gyp:gfx_test_support',
              '../ui/gfx/gfx.gyp:gfx_geometry',
              '../ui/gl/gl.gyp:gl',
              'content.gyp:content',
            ],
            'include_dirs': [
              '<(DEPTH)/third_party/khronos',
            ],
            'sources': [
              'common/gpu/media/android_video_decode_accelerator_unittest.cc',
              'common/gpu/media/rendering_helper.h',
              'common/gpu/media/rendering_helper.cc',
              'common/gpu/media/video_accelerator_unittest_helpers.h',
              'common/gpu/media/video_decode_accelerator_unittest.cc',
            ],
            'conditions': [
              ['OS=="android"', {
                'sources/': [
                  ['exclude', '^common/gpu/media/rendering_helper.h'],
                  ['exclude', '^common/gpu/media/rendering_helper.cc'],
                  ['exclude', '^common/gpu/media/video_decode_accelerator_unittest.cc'],
                ],
                'dependencies': [
                  '../media/media.gyp:player_android',
                  '../testing/gmock.gyp:gmock',
                  '../testing/android/native_test.gyp:native_test_native_code',
                  '../gpu/gpu.gyp:gpu_unittest_utils',
                ],
              }, { # OS!="android"
                'sources/': [
                  ['exclude', '^common/gpu/media/android_video_decode_accelerator_unittest.cc'],
                ],
              }],
              ['OS=="win"', {
                'dependencies': [
                  '<(angle_path)/src/angle.gyp:libEGL',
                  '<(angle_path)/src/angle.gyp:libGLESv2',
                ],
              }],
              ['(OS=="win" and win_use_allocator_shim==1) or '
               '(os_posix == 1 and OS != "android" and '
               ' use_allocator!="none")', {
                'dependencies': [
                  '../base/allocator/allocator.gyp:allocator',
                ],
              }],
              ['target_arch != "arm" and (OS=="linux" or chromeos == 1)', {
                'include_dirs': [
                  '<(DEPTH)/third_party/libva',
                ],
              }],
              ['use_x11==1', {
                'dependencies': [
                  '../build/linux/system.gyp:x11',  # Used by rendering_helper.cc
                  '../ui/gfx/x/gfx_x11.gyp:gfx_x11',
                ],
              }],
            ],
            # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
            'msvs_disabled_warnings': [ 4267, ],
          },
        ]
    }],
    ['chromeos==1 and use_x11 == 1 and target_arch != "arm"', {
      'targets': [
          {
            'target_name': 'vaapi_h264_decoder_unittest',
            'type': '<(gtest_target_type)',
            'dependencies': [
              'content.gyp:content_common',
              '../base/base.gyp:base',
              '../build/linux/system.gyp:x11',
              '../media/media.gyp:media',
              '../testing/gtest.gyp:gtest',
              '../third_party/libyuv/libyuv.gyp:libyuv',
              '../ui/gfx/gfx.gyp:gfx_geometry',
            ],
            'sources': [
              'common/gpu/media/vaapi_h264_decoder_unittest.cc',
            ],
            'include_dirs': [
              '<(DEPTH)/third_party/libva',
            ],
          },
        ]
    }],
    ['chromeos==1 and (target_arch == "arm" or use_x11 == 1)', {
      'targets': [
        {
          'target_name': 'video_encode_accelerator_unittest',
          'type': 'executable',
          'dependencies': [
            '../base/base.gyp:base',
            '../media/media.gyp:media',
            '../media/media.gyp:media_test_support',
            '../testing/gtest.gyp:gtest',
            '../ui/base/ui_base.gyp:ui_base',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
            '../ui/gfx/gfx.gyp:gfx_test_support',
            '../ui/gl/gl.gyp:gl',
            'content.gyp:content',
          ],
          'sources': [
            'common/gpu/media/video_accelerator_unittest_helpers.h',
            'common/gpu/media/video_encode_accelerator_unittest.cc',
          ],
          'include_dirs': [
            '<(DEPTH)/third_party/libva',
            '<(DEPTH)/third_party/libyuv',
          ],
          'conditions': [
            ['use_x11==1', {
              'dependencies': [
                '../ui/gfx/x/gfx_x11.gyp:gfx_x11',
              ],
            }],
          ],
        },
      ]
    }],
    ['OS == "android"', {
      'targets': [
        {
          # TODO(GN)
          'target_name': 'content_gl_tests_apk',
          'type': 'none',
          'dependencies': [
            'content_gl_tests',
            'content_java_test_support',
          ],
          'variables': {
            'test_suite_name': 'content_gl_tests',
          },
          'includes': [
            '../build/apk_test.gypi',
          ],
        },
        {
          # TODO(GN)
          'target_name': 'content_unittests_apk',
          'type': 'none',
          'dependencies': [
            'content.gyp:content_java',
            'content_unittests',
          ],
          'variables': {
            'test_suite_name': 'content_unittests',
          },
          'includes': [ '../build/apk_test.gypi' ],
        },
        {
          # TODO(GN)
          'target_name': 'content_browsertests_apk',
          'type': 'none',
          'dependencies': [
            'content.gyp:content_icudata',
            'content.gyp:content_java',
            'content_browsertests',
            'content_java_test_support',
            'content_shell_java',
          ],
          'variables': {
            'apk_name': 'content_browsertests',
            'java_in_dir': 'shell/android/browsertests_apk',
            'resource_dir': 'shell/android/browsertests_apk/res',
            'native_lib_target': 'libcontent_browsertests',
            'additional_input_paths': ['<(PRODUCT_DIR)/content_shell/assets/content_shell.pak'],
            'asset_location': '<(PRODUCT_DIR)/content_shell/assets',
            'conditions': [
              ['icu_use_data_file_flag==1', {
                'additional_input_paths': [
                  '<(PRODUCT_DIR)/icudtl.dat',
                ],
              }],
            ],
          },
          'includes': [ '../build/java_apk.gypi' ],
        },
        {
          # TODO(GN)
          'target_name': 'content_perftests_apk',
          'type': 'none',
          'dependencies': [
            'content.gyp:content_java',
            'content_perftests',
          ],
          'variables': {
            'test_suite_name': 'content_perftests',
          },
          'includes': [ '../build/apk_test.gypi' ],
        },
        {
          # GN: //content/shell/android:chromium_linker_test_apk
          'target_name': 'chromium_linker_test_apk',
          'type': 'none',
          'conditions': [
            ['target_arch != "x64" and target_arch != "arm64"', {
              'dependencies': [
                'chromium_android_linker_test',
                'content.gyp:content_icudata',
                'content.gyp:content_java',
                'content_shell_java',
              ],
              'variables': {
                'apk_name': 'ChromiumLinkerTest',
                'java_in_dir': 'shell/android/linker_test_apk',
                'resource_dir': 'shell/android/linker_test_apk/res',
                'native_lib_target': 'libchromium_android_linker_test',
                'additional_input_paths': ['<(PRODUCT_DIR)/content_shell/assets/content_shell.pak'],
                'asset_location': '<(PRODUCT_DIR)/content_shell/assets',
                'use_chromium_linker': '1',
                'enable_chromium_linker_tests': '1',
                'conditions': [
                  ['icu_use_data_file_flag==1', {
                    'additional_input_paths': [
                      '<(PRODUCT_DIR)/icudtl.dat',
                    ],
                  }],
                ],
              },
              'includes': [ '../build/java_apk.gypi' ],
            },
           ],
          ],
        },
        {
          # GN: //content/shell/android:linker_test
          'target_name': 'chromium_android_linker_test',
          'type': 'shared_library',
          'defines!': ['CONTENT_IMPLEMENTATION'],
          'dependencies': [
            'chromium_android_linker_test_jni_headers',
            'content_shell_lib',
            # Required to include "content/public/browser/android/compositor.h"
            # in chromium_linker_test_android.cc :-(
            '../skia/skia.gyp:skia',
          ],
          'sources': [
            'shell/android/linker_test_apk/chromium_linker_test_android.cc',
            'shell/android/linker_test_apk/chromium_linker_test_linker_tests.cc',
          ],
        },
        {
          # GN: //content/shell/android:linker_test_jni_headers
          'target_name': 'chromium_android_linker_test_jni_headers',
          'type': 'none',
          'sources': [
            'shell/android/linker_test_apk/src/org/chromium/chromium_linker_test_apk/LinkerTests.java',
          ],
          'variables': {
            'jni_gen_package': 'content/shell',
          },
          'includes': [ '../build/jni_generator.gypi' ],
        },
        {
          # TODO(GN)
          'target_name': 'video_decode_accelerator_unittest_apk',
          'type': 'none',
          'dependencies': [
            'video_decode_accelerator_unittest',
          ],
          'variables': {
            'test_suite_name': 'video_decode_accelerator_unittest',
          },
          'includes': [ '../build/apk_test.gypi' ],
        },
        {
          # GN: //content/public/test/android:test_support_content_jni_headers
          'target_name': 'test_support_content_jni_headers',
          'type': 'none',
          'sources': [
            'public/test/android/javatests/src/org/chromium/content/browser/test/NestedSystemMessageHandler.java',
          ],
          'variables': {
            'jni_gen_package': 'content/public/test',
          },
          'includes': [ '../build/jni_generator.gypi' ],
        },
        {
          # GN: //content/public/test/android:content_java_test_support
          'target_name': 'content_java_test_support',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base',
            '../base/base.gyp:base_java_test_support',
            'content.gyp:content_common',
            'content.gyp:content_java',
          ],
          'variables': {
            'java_in_dir': '../content/public/test/android/javatests',
          },
          'includes': [ '../build/java.gypi' ],
        },
        {
          # GN: //content/shell/android:content_shell_test_apk
          #     and //content/public/android:content_javatests
          'target_name': 'content_shell_test_apk',
          'type': 'none',
          'dependencies': [
            'content_java_test_support',
            'content_shell_apk_java',
            'content.gyp:content_java',
            '../base/base.gyp:base_java',
            '../base/base.gyp:base_javatests',
            '../base/base.gyp:base_java_test_support',
            '../media/media.gyp:media_java',
            '../media/media.gyp:media_test_support',
            '../mojo/public/mojo_public.gyp:mojo_public_test_interfaces',
            '../net/net.gyp:net_java',
            '../net/net.gyp:net_javatests',
            '../net/net.gyp:net_java_test_support',
          ],
          'variables': {
            'apk_name': 'ContentShellTest',
            'java_in_dir': 'shell/android/javatests',
            'resource_dir': 'shell/android/shell_apk/res',
            'additional_src_dirs': ['public/android/javatests/',],
            'is_test_apk': 1,
          },
          'includes': [ '../build/java_apk.gypi' ],
        },
      ],
    }],
    ['OS!="android" and OS!="ios" and OS!="linux"', {
      # npapi test plugin doesn't build on android or ios
      'targets': [
        {
          'target_name': 'npapi_test_plugin',
          'type': 'loadable_module',
          'variables': {
            'chromium_code': 1,
          },
          'mac_bundle': 1,
          'dependencies': [
            '<(DEPTH)/base/base.gyp:base',
            '<(DEPTH)/third_party/icu/icu.gyp:icuuc',
            '<(DEPTH)/third_party/npapi/npapi.gyp:npapi',
          ],
          'sources': [
            'test/plugin/npapi_constants.cc',
            'test/plugin/npapi_constants.h',
            'test/plugin/npapi_test.cc',
            'test/plugin/npapi_test.def',
            'test/plugin/npapi_test.rc',
            'test/plugin/plugin_arguments_test.cc',
            'test/plugin/plugin_arguments_test.h',
            'test/plugin/plugin_client.cc',
            'test/plugin/plugin_client.h',
            'test/plugin/plugin_create_instance_in_paint.cc',
            'test/plugin/plugin_create_instance_in_paint.h',
            'test/plugin/plugin_delete_plugin_in_deallocate_test.cc',
            'test/plugin/plugin_delete_plugin_in_deallocate_test.h',
            'test/plugin/plugin_delete_plugin_in_stream_test.cc',
            'test/plugin/plugin_delete_plugin_in_stream_test.h',
            'test/plugin/plugin_execute_stream_javascript.cc',
            'test/plugin/plugin_execute_stream_javascript.h',
            'test/plugin/plugin_get_javascript_url_test.cc',
            'test/plugin/plugin_get_javascript_url_test.h',
            'test/plugin/plugin_get_javascript_url2_test.cc',
            'test/plugin/plugin_get_javascript_url2_test.h',
            'test/plugin/plugin_geturl_test.cc',
            'test/plugin/plugin_geturl_test.h',
            'test/plugin/plugin_javascript_open_popup.cc',
            'test/plugin/plugin_javascript_open_popup.h',
            'test/plugin/plugin_new_fails_test.cc',
            'test/plugin/plugin_new_fails_test.h',
            'test/plugin/plugin_npobject_identity_test.cc',
            'test/plugin/plugin_npobject_identity_test.h',
            'test/plugin/plugin_npobject_lifetime_test.cc',
            'test/plugin/plugin_npobject_lifetime_test.h',
            'test/plugin/plugin_npobject_proxy_test.cc',
            'test/plugin/plugin_npobject_proxy_test.h',
            'test/plugin/plugin_request_read_test.h',
            'test/plugin/plugin_request_read_test.cc',
            'test/plugin/plugin_schedule_timer_test.cc',
            'test/plugin/plugin_schedule_timer_test.h',
            'test/plugin/plugin_setup_test.cc',
            'test/plugin/plugin_setup_test.h',
            'test/plugin/plugin_test.cc',
            'test/plugin/plugin_test.h',
            'test/plugin/plugin_test_factory.h',
            'test/plugin/plugin_thread_async_call_test.cc',
            'test/plugin/plugin_thread_async_call_test.h',
            'test/plugin/plugin_windowed_test.cc',
            'test/plugin/plugin_windowed_test.h',
            'test/plugin/plugin_private_test.cc',
            'test/plugin/plugin_private_test.h',
            'test/plugin/plugin_test_factory.cc',
            'test/plugin/plugin_window_size_test.cc',
            'test/plugin/plugin_window_size_test.h',
            'test/plugin/plugin_windowless_test.cc',
            'test/plugin/plugin_windowless_test.h',
            'test/plugin/resource.h',
          ],
          'include_dirs': [
            '../..',
          ],
          'xcode_settings': {
            'INFOPLIST_FILE': '<(DEPTH)/content/test/plugin/Info.plist',
          },
          'conditions': [
            ['OS!="win"', {
              'sources!': [
                # TODO(port):  Port these.
                # plugin_npobject_lifetime_test.cc has win32-isms
                #   (HWND, CALLBACK).
                'test/plugin/plugin_npobject_lifetime_test.cc',
                 # The window APIs are necessarily platform-specific.
                'test/plugin/plugin_window_size_test.cc',
                'test/plugin/plugin_windowed_test.cc',
                 # Seems windows specific.
                'test/plugin/plugin_create_instance_in_paint.cc',
                'test/plugin/plugin_create_instance_in_paint.h',
                 # windows-specific resources
                'test/plugin/npapi_test.def',
                'test/plugin/npapi_test.rc',
              ],
            }],
            ['OS=="mac"', {
              'product_extension': 'plugin',
              'link_settings': {
                'libraries': [
                  '$(SDKROOT)/System/Library/Frameworks/Carbon.framework',
                ],
              },
            }],
            ['os_posix == 1 and OS != "mac" and (target_arch == "x64" or target_arch == "arm")', {
              # Shared libraries need -fPIC on x86-64
              'cflags': ['-fPIC']
            }],
          ],
        },
        {
          'target_name': 'copy_npapi_test_plugin',
          'type': 'none',
          'dependencies': [
            'npapi_test_plugin',
          ],
          'conditions': [
            ['OS=="win"', {
              'copies': [
                {
                  'destination': '<(PRODUCT_DIR)/plugins',
                  'files': ['<(PRODUCT_DIR)/npapi_test_plugin.dll'],
                },
              ],
            }],
            ['OS=="mac"', {
              'copies': [
                {
                  'destination': '<(PRODUCT_DIR)/plugins/',
                  'files': ['<(PRODUCT_DIR)/npapi_test_plugin.plugin'],
                },
              ]
            }],
            ['os_posix == 1 and OS != "mac"', {
              'copies': [
                {
                  'destination': '<(PRODUCT_DIR)/plugins',
                  'files': ['<(PRODUCT_DIR)/libnpapi_test_plugin.so'],
                },
              ],
            }],
          ],
        },
      ],
    }],
  ],
}
