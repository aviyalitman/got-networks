'''
SQL Queries used in the Python script.
'''

CREATE TABLE all_edges AS
    SELECT source, target FROM got_edges
    UNION 
    SELECT target, source FROM got_edges;

CREATE TABLE one_hop AS
    SELECT s.source as one_source, s.target as one_target, t.source as two_source, t.target as two_target
		FROM all_edges as s
		JOIN
		all_edges as t
		ON s.target=t.source 
    WHERE s.source=character1 or s.source=character2;

CREATE TABLE two_hop AS
    SELECT a.two_source, a.two_target, b.source as one_source_1, b.target as one_target_1
    FROM 
		one_hop as a
		JOIN 
        all_edges as b
		ON a.two_target=b.source
    WHERE b.target=character1 or b.target=character2;

SELECT a.one_source, a.one_target, a.two_source, a.two_target, b.one_source_1, b.one_target_1 
	FROM 
		one_hop as a
		JOIN 
		two_hop as b
		ON a.two_target=b.two_target and a.two_source=b.two_source
    WHERE a.one_source != b.one_target_1;