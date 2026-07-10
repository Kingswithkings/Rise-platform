# Backend Application

Feature packages own their routes, schemas, services, repositories, and models. Shared
infrastructure belongs in `core`, `database`, or `shared`; feature-specific behavior must
not leak into those packages.
