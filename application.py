from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return ''' 
        <h3>Deploying an app through AWS</h3>
        <p>Using Flask application and deploying it through ElasticBeanStalk -- assisted by Code pipelines for automation'
        </p>
    ''' 
if __name__ == '__main__':
    application.run(debug=True)
