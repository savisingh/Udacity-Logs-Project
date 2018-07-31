#!/usr/lib python2.7
import psycopg2
import time


def get_popular_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # the following query returns the most popular three articles of all time
    c.execute("select articles.title, populararticles.count from "
              "populararticles, articles "
              "where articles.slug = populararticles.replace;")
    articles = c.fetchall()
    db.close()
    print("\"%s\" - %d views" % (articles[0][0], articles[0][1]))
    print("\"%s\" - %d views" % (articles[1][0], articles[1][1]))
    print("\"%s\" - %d views" % (articles[2][0], articles[2][1]))
    print('\n')
    return articles


def get_popular_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # the following query returns the most popular article authors of all time
    c.execute("select name, SUM(count) from authorarticlecount "
              "group by name order by sum desc;")
    authors = c.fetchall()
    db.close()
    print("%s - %d views" % (authors[0][0], authors[0][1]))
    print("%s - %d views" % (authors[1][0], authors[1][1]))
    print("%s - %d views" % (authors[2][0], authors[2][1]))
    print("%s - %d views" % (authors[3][0], authors[3][1]))
    print('\n')
    return authors


def get_error_days():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # the following query returns the days where more than 1% of requests
    # lead to errors
    c.execute("select okdate, percentage from errorpercentages "
              "where percentage>1;")
    days = c.fetchall()
    db.close()
    ts = days[0][0]
    print(ts.strftime("%B %d, %Y") + " - %d%% errors" % (days[0][1]))
    return days

get_popular_articles()
get_popular_authors()
get_error_days()
