## Continuous Integration and Deployment

### Testing Strategy

The testing strategy for any ML sytem should be only restricted to the inference API.
Unit tests should ideally be the only metric being implemented in the CI/CD pipeline

Integration tests can be done at a dedicated testing layer only after the new deployment is done.

Stress/Load Testing should be done only in an environment which closely resembles the Production Environment so that we can get near-realtime results.

### Deployment Automation

Standard CI Pipelines can be used for the deployment based on the target environment and can be customised based on the requirement. The pipeline would also include the unit tests in consideration or in case of failure in unit tests, will result in a build failure

### Security Checks

Primary components which chould be checked are:

1. Libraries: The libraries being used by the service could have vulnerabilites in them and should be scanned
2. Docker image scan: The docker image in question may have some binaries which have a reported CVE and should be resolved before deployment
3. Static Analayis: The code may have certain vulnerabilites which may expose us to certain vulnerabilites and should be resolved first