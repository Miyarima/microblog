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

## [11.3.0] - 2024-12-05

### Added

- Bandit, Trivy and Dockle for finding security vulnerabilities
- Technical study about [Datadog](https://www.datadoghq.com/)

### Fixed

- Security issues found by Bandit, Trivy and Dockle

### Changed

- Security groups to only allow trafic from each other on ports other than 22, 80 and 443
- SSH configuration on all servers now based on Mozilla OpenSSH 6.7+

## [11.2.3] - 2024-11-28

### Added

- A recod for the database
- A new playbook for creating appserver(s) in sequence with rolling release

## [11.1.2] - 2024-11-28

### Fixed

- Wrong name on version variable
- a lot of bugs

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
