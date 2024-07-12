import boto3

elb= boto3.client('elbv2')

load_balancer= elb.create_load_balancer(
    Name = 'test',
    Subnets = [
        '<subnet-id-1>',
        '<subnet-id-2>',
    ],
    SecurityGroups = [
        '<security-group-1>',
    ],
    Type='application'
)

tg = elb.create_target_group(
    Name = 'test-tg',
    Protocol = 'HTTP',
    Port = 80,
    VpcId = '<vpc-id-1>'
)

register = elb.register_targets(
    TargetGroupArn = '<target-group-arn-1>',
    Targets = [
        {
            'Id' : '<ec2-instance-id>'
        },
    ]
)

listener = elb.create_listener(
    LoadBalancerArn = '<load-balancer-arn>',
    DefaultActions = [
        {
            'TargetGroupArn': '<target-group-arn>',
            'Type' : 'forward'
        },
    ],
    Port = 80,
    Protocol = 'HTTP'
)