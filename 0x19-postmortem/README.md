### ISSUE SUMMARY:
    Duration of outage: Dec 13, 2023. 02:00 pm - Dec 13, 2023. 05:30 pm (WAT)
    Impact due to outage: ordering service went down, users were unable to place orders, 75% of users were unable to access the ordering page/ 25% were able to view the order page but the checkout button was unresponsive.
    root cause: break in the js script due to unexpected event

### TIMELINE:
* 02:02 pm - Issue Detected.
* Detection Method: Monitoring system triggered alerts for service unavailability.
* 02:05 pm to 03:15pm - Actions Taken: The incident response team immediately investigated the issue, focusing on the core infrastructure components and network connectivity. (Parts invested, engine, console, api, models).
* Misleading Investigation: The team initially suspected a network issue due to increased latency, leading them to investigate switches and routers for potential malfunctions.
* 03:16pm to 04:00pm - Escalation: As the investigation progressed, the incident was escalated to the network engineering team to further analyze and troubleshoot the potential network issue.
* 04:02pm to 05:20pm - Resolution: Upon closer inspection, it was discovered that the root cause was not a network outage but an  unanticipated fail in source file. The incident response team quickly resolved the issue by analyzing and testing all script within the dynamic framework, fixed the code, tested it and queried it in to substistute for the rush time of the high demand shopping while writting a new, improved, roburst and thoroughly tested code to replace the broken one.
### ROOT CAUSE AND RESOLUTION:
* the root cause was majorly by a runtime error that wasn't properly accounted for which resulted in a conflicting rangeerror which was handled and now causing unforeseen issues.
* to resolve this issue, thorough testing was done in new scenerios and also old ones, each error was handled indivily and also collectively to ensure a work module.
### CORRECTIVE AND PREVENTIVE MEASURES
* Most test in various edge cases would be properly handled, each error would be handle individually and collectively
* -test
  -test
  -test
  -test
