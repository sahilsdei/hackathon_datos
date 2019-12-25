import os,json
from flask import Flask, Response, render_template, make_response, request, jsonify
from flask_restplus import Api, Resource
from scraper import get_links, get_detail,get_quote
from hashtag_topic_modeling import get_hashtag,get_summary
PORT = os.environ.get('PORT') or  8001
app = Flask(__name__)

api = Api(app, version='1.0', title='Smart Tweet',
          description='Twitter API',
          )

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))

@api.route('/index')
class Index(Resource):
    def get(self):
        print("hello")
        dict ={"Hello, world!"}
        return Response(dict)

def prepdata():
    _dict = {
        "tech": [],
        "quotes": []
    }
    for link in get_links()[:5]:
        detail_txt = get_detail(link=link['link'])
        raw_hashtabs = get_hashtag(detail_txt)[0]
        hashtags=[]
        for a in raw_hashtabs[1].split('+'):
           b = a.split('*')[1].replace(' ', '').replace('"', '')
           hashtags.append('#'+b)

        _dict['tech'].append({
            "title":link['text'],
            "hashtags":hashtags[:5],
            "summary":get_summary(detail_txt),
            "link":link['link']
        })

        _dict['quotes'] = get_quote()
    return _dict

@api.route('/getLinks')
class Links(Resource):
    def get_links(self):
        content = get_links()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html',
                                             context=content
                                             ), 200, headers)

@api.route('/getLinktText')
class LinkDetail(Resource):
    def get(self):
        link = request.args.get('link')
        content = get_detail(link=link)
        tags = get_hashtag([get_detail(link=link)])
        summary = get_summary([content])
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html',
                                             context=content,
                                             tags = tags,
                                             summary = summary
                                             ), 200, headers)

@api.route('/get_tweets')
class GetJson(Resource):
    def get(self):
        return jsonify(prepdata())
        #return jsonify(get_quote())

@api.route('/dummy_tweets')
class GetDummy(Resource):
    def get(self):
        with open('dumy.json') as f:
            data = json.load(f)
            return jsonify(data)

@api.route('/single_tweet')
class GetSingleDummy(Resource):
    def get(self):
        tnum = 0
        tnum = request.args.get('tnum')
        print('tnum',type(tnum))
        with open('dumy.json') as f:
            data = json.load(f)
            return jsonify(data['tech'][int(tnum)])


if __name__ == "__main__":
    #app.config['DEBUG'] = os.environ.get('ENV') == 'development'
    app.run(host='0.0.0.0', port=int(PORT))
