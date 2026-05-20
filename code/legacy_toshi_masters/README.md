# Legacy Toshi_MASTERS Code

This directory contains the legacy Python/QGIS scripts found in the local paper source folder for `paper-2019-13`. They are preserved as source code for audit and archive review.

The scripts were written for an older Python 2/QGIS environment and contain hard-coded original workstation paths such as `/Users/toshiyokoo/Desktop/...`. They are not expected to run without path adaptation, dependency installation, and separately obtained TBI and MetroGIS inputs.

No GPS traces, person records, survey records, street-network shapefiles, or derived participant-level outputs are included here.

Primary workflow order is implied by the numeric prefixes: trip generation, region/speed filters, mode identification, coordinate conversion, TBI matching, map matching, child/zero-speed-limit removal, summarization, compile steps, and fixed-effects preparation.

Updated: 2026-05-18 00:02:14
