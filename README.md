# aws-monitoring-tools
AWS monitoring tools

# Example of config

Must be inside a file named `conf.config`

```
[sqs-tuttiflirty]
aws_access_key: 
aws_secret_key: 
aws_region: eu-west-1
queue: https://sqs.eu-west-1.amazonaws.com/my/queue
check_method: stuck
alert_method: email
email_to: me@me.com

[email]
aws_access_key: 
aws_secret_key: 
aws_region: eu-west-1
from: me@me.com
```