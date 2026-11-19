# Release v1.1.0

## Added
- Special base delivery rate of 80.0 for Kyiv.
- Explicit `tax_rate` parameter (default 0.20) for invoice processing.

## Changed
- Delivery weight coefficient increased from 12.0 to 15.0.
- Billing module refactored to Data Coupling: `calculate_delivery_cost` now takes `city` and `weight_kg` instead of the whole `CustomerProfile`.

## Breaking Changes
- Function signatures of the delivery cost calculation have changed.
- Removed the global variable `GLOBAL_TAX_RATE`.
- Removed the `mode_flag` parameter: `process_invoice` is split into `process_standard_invoice` and `process_tax_exempt_invoice`.
