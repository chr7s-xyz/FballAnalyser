from flask import Flask,request,render_template,session,redirect
import pandas

app=Flask(__name__,template_folder='templates')


df=pandas.read_csv("fifa_players.csv")


@app.route('/',methods=("POST","GET"))
def html_table():
    return render_template("index.html")


@app.route('/result',methods=("POST","GET"))
def res():
    
    df2=df[df['name'].isin([request.form['name']])]
    df3=df[df['nationality'].isin([request.form['country']])]
    df4=df[df['positions'].apply(lambda x: request.form['position'] in x)]
    df5=df4[df4['nationality'].isin([request.form['country']])]
   
    
    if (request.form['country']=='') & (request.form['position']=='') & (request.form['name'] != ''):
        return render_template('index.html',column_names=df2.columns.values, row_data=list(df2.values.tolist()), zip=zip)
    elif (request.form['country'] != '') & (request.form['position']=='') & (request.form['name'] == ''):
        return render_template("resultn.html",tables=[df3.to_html(classes='data')],titles=df3.columns.values)
    elif (request.form['position'] != '') & (request.form['country'] == '') & (request.form['name'] == ''):
        return render_template("resultn.html",tables=[df4.to_html(classes='data')],titles=df4.columns.values)
    elif (request.form['position'] != '') & (request.form['country'] != ''):
        return render_template("resultn.html",tables=[df5.to_html(classes='data')],titles=df5.columns.values)
    else:
        return render_template('resultn.html')
    





if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')