# ADR-009

## Title

Hierarchical Category Architecture

## Status

Accepted

## Context

RISE requires a scalable category structure for products and services.

## Decision

Use a self-referencing parent_id to support unlimited category depth.

## Alternatives

Separate tables per level.

## Reason

Self-referencing tables are simpler, more flexible, and easier to maintain.

## Consequences

Recursive queries may be required for tree views.
