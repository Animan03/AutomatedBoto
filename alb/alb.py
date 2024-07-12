import boto3

elb= boto3.client('elbv2')

load_balancer= elb.create_load_balancer(
    Name = 'test',
    Subnets = [
        'subnet-0dcb0c34f00f5b45d',
        'subnet-02caad7c757855768',
    ],
    SecurityGroups = [
        'sg-095603a3e2678aca4',
    ],
    Type='application'
)

tg = elb.create_target_group(
    Name = 'test-tg',
    Protocol = 'HTTP',
    Port = 80,
    VpcId = 'vpc-0519d6821089bfbe0'
)

register = elb.register_targets(
    TargetGroupArn = 'arn:aws:elasticloadbalancing:ap-south-1:851725512255:targetgroup/test-tg/81fbd6a826b4c437',
    Targets = [
        {
            'Id' : 'i-0104ddce9afc52d12'
        },
    ]
)

listener = elb.create_listener(
    LoadBalancerArn = 'arn:aws:elasticloadbalancing:ap-south-1:851725512255:loadbalancer/app/test/a7dadb2e7d789457',
    DefaultActions = [
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:ap-south-1:851725512255:targetgroup/test-tg/81fbd6a826b4c437',
            'Type' : 'forward'
        },
    ],
    Port = 80,
    Protocol = 'HTTP'
)