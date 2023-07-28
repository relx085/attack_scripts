# AMP-Methods

## Research on UDP/TCP amplification vectors, payloads and mitigations

**The subfolders in this repository will contain the following:**

* Overview README.md
  * Name, Ports, Amplification factors, Update Info
  * Request <> Response Example with test IP (netcat yay!)
  * Potential official documentation
  * Potential mitigation strategies
* The raw payload (e.g. for use in zmap) OR potential scanning script (C).
* Raw socket flood script (C) for analysis to build flowspec or ACL mitigations.

## What is "amplification" in respect to Denial of Service? Give me an Example!

Amplification is where well-formed or malformed socket or application data requests elicit a response larger than the input data. This can then be abused to "amplify" a request, usually by means of Distributed Reflected Denial of Service (DRDoS) attacks. This distinction is usually lumped under the one banner of "DDoS"; however the former indicates that the traffic does not directly come from bots or single servers but is reflected off of usually benign services, thus typically rendering blacklists and simple firewall solutions useless.

## Compiling the C?

General C scripts:

```bash
gcc -pthread -O2 -o binary file.c
```

TCP scripts (requires 32bit compilation to avoid invalid checksum function return values):

```bash
gcc -m32 -pthread -O2 -o binary file.c
```
