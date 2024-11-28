# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Types of changes

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

---

## [11.1.1] - 2024-11-28

### Fixed

- Wrong file name for version page

## [11.1.0] - 2024-11-28

### Added

- Two appservers to distubute load between
- A subdomain for each appserver
- Credentials for creating servers (VM) with anisible
- Ansible playbook for running mysql in docker container
- Ansible playbook for running appserver(s) in docker container
- Ansible playbook for running a load balancer with nginx
- A new route in microblog to preview current version
- A plethora of small fixes

### Fixed

- 100+ lint issues with yaml files

## [11.0.0] - 2024-11-15

### Added

- v11.0.0 Dockerfile for prod and testing
- v11.0.0 Docker compose file for running application and tests
- v11.0.0 Template for structuring git commits
- v11.0.0 Workflow for running test and publishing docker containers
- v11.0.0 Following other users in the application, with corresponing test for this feature
