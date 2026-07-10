# Backup and Recovery

PostgreSQL requires encrypted automated backups, retention policies, and point-in-time
recovery appropriate to the environment. Configuration and Redis recovery requirements
must also be documented.

## Required controls

- Defined recovery point and recovery time objectives
- Automated backup verification
- Restricted backup access
- Regular restore exercises
- Documented incident ownership and recovery procedure

No production launch is complete until a restore has been successfully tested.
