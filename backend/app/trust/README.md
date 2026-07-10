# 1stKings Trust

1stKings Trust is the verification and reputation layer inside RISE.

## Purpose

It helps buyers identify trustworthy sellers, businesses, and service providers.

The public brand is always **1stKings Trust**. Code remains under `app/trust/`.

## Reputation architecture

Trust events are the source of truth. The 1stKings Trust Score and 1stKings Trust Badge
are calculated from the immutable event history; the score is not stored on the profile.

`Trust Profile → Trust Events → 1stKings Trust Score → 1stKings Trust Badge`

## MVP Features

- Trust profile
- Trust ID
- Trust score
- Business verification
- Reviews
- Trust events
- Verified badge

## Future Features

- AI fraud detection
- Document verification
- Dispute management
- Standalone 1stKings Trust API
- Blockchain audit trail
