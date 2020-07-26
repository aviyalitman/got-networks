import pandas as pd
import json
import pymysql
import secret_info as si

conn = pymysql.connect(
    host="localhost",
    user=si.user,
    password=si.password,
    db=si.db,
    cursorclass=pymysql.cursors.DictCursor)


def run_q(sql, args=None, fetch=True, cur=None, conn=conn):
    '''
    Helper function to run an SQL statement.
    
    Parameters
    __________
    
    sql : SQL template with placeholders for parameters. Cannot be NULL.
    args : Values to pass with statement. May be null.
    fetch : Execute a fetch and return data if TRUE.
    conn : The database connection to use. This cannot be NULL, unless a cursor is passed.   
    cur : The cursor to use. 

    Returns
    _______
    
    A pair of the form (execute response, fetched data). There will only be fetched data if
        the fetch parameter is True. 'execute response' is the return from the connection.execute, which
        is typically the number of rows effected.
    '''
    cursor_created = False
    connection_created = False

    try:
        if conn is None:
            raise ValueError("In this implementation, conn cannot be None.")

        if cur is None:
            cursor_created = True
            cur = conn.cursor()

        if args is not None:
            log_message = cur.mogrify(sql, args)
        else:
            log_message = sql

        res = cur.execute(sql, args)

        if fetch:
            data = cur.fetchall()
        else:
            data = None

    except Exception as e:
        raise(e)

    return (res, data)


def drop_tables(table_list):
    '''
    A helper function to drop tables, which is necessary after executing the queries.
    '''
    for table in table_list:
        q = "drop table if exists {}".format(table)
        res,d = run_q(q)


def all_edges():
    '''
    got-edges only contains one way relationships. We want all interactions, so we are
    going to disregard direction in this graph. This SQL function will find all 
    bi-directional first degree relationships between characters.
    '''
    
    q = """CREATE TABLE all_edges AS
        SELECT source, target FROM got_edges
        UNION 
        SELECT target, source FROM got_edges"""

    res,d = run_q(q)


def one_hop(character1, character2):
    '''
    SQL function to find second degree relationships between characters.
    '''
    
    q = """CREATE TABLE w4111midterm.one_hop AS 
        SELECT s.source as one_source, s.target as one_target, t.source as two_source, t.target as two_target 
        FROM W4111Midterm.all_edges as s 
        JOIN w4111Midterm.all_edges as t 
        on s.target=t.source 
        WHERE s.source=%s OR s.source=%s"""
    
    res,d = run_q(q, args=(character1, character2))


def two_hop(character1, character2):
    '''
    SQL function to find third degree relationships between characters. 
    '''

    q = """CREATE TABLE w4111midterm.two_hop AS 
        SELECT a.two_source, a.two_target, b.source as one_source_1, b.target as one_target_1 
        FROM w4111midterm.one_hop as a 
        JOIN w4111midterm.all_edges as b 
        on a.two_target=b.source 
        WHERE b.target=%s OR b.target=%s"""
    
    res,d = run_q(q, args=(character1, character1))

