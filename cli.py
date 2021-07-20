import click
import yaml

@click.command()
@click.option('-n', required=True,type=str, help='Your node name')
@click.option('-s','-subscribe_name', required=True, help='Your subscribe topic')
@click.option('-p','-publish_name', required=True, help='Your publish topic')
def rospy(n,s,p):
    data = {
        "node_name":n,
        "subscribed_topic_name":s,
        "publish_topic_name":p
    }
    with open('node_config.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    
if __name__ == '__main__':
    rospy()