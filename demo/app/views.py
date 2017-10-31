from app import app
import os
from flask import render_template
from flask import Flask, redirect, url_for, request, send_from_directory
from flask import json
import sys
import sys
import csv


curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
parDir = os.path.abspath(os.path.join(curDir, os.pardir))
tmpDir = os.path.abspath(os.path.join(curDir,'tmp/'))
resultFile=os.path.abspath(os.path.join(parDir,'results.csv'))
crawlerFile=os.path.abspath(os.path.join(curDir, os.pardir,os.pardir,'run_crawler_demo.py'))




class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",title='Home')


@app.route('/search_results',methods = ['POST'])
def search_results():
    if request.method == 'POST':
          os.system('python '+crawlerFile+' '+ request.json['product'])
          print 'Crawling Completed'
          title=[]
          image=[]
          price=[]
          url=[]
          source=[]
          with open(resultFile) as f:
            records = csv.DictReader(f)
            for row in records:
                title.append(row['product_name'])
                image.append(row['image_url'])
                price.append(row['price'])
                url.append(row['product_url'])
                source.append(row['source'])
          data=dict({'product_name':title,'image_url':image,'price':price,'product_url':url,'source':source})
          response = app.response_class(
            response=json.dumps(data, cls=MyEncoder),
            status=200,
            mimetype='application/json'
        )
          return response