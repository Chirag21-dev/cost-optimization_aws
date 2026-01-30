import boto3

ec2=boto3.client('ec2')

def lambda_handler(event, context):
   response = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
   unused_volume=[]
   for volume in response['Volumes']:
      unused_volume.append({                                                  
         'VolumeId': volume['VolumeId'],
         'Size': volume['Size'],
         'AvailabilityZone': volume['AvailabilityZone'],
            'State': volume['State']
      })
   return {
      "statusCode": 200,
      "unused_volumes": unused_volume,
      "number_of_unused_volumes": len(unused_volume)}