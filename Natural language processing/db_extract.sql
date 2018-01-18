-- extract articles with named entities
-- columns articleId, entity name, entity type name and article text
SELECT 
	pa.project_article_id AS 'id',
	et.name AS 'type',
	e.name AS 'name',
	REPLACE(CONCAT(a.title, ' ', a.body), '"', '\"') AS 'text'
FROM
	`project_article` AS pa
INNER JOIN 
	`article` AS a ON pa.article_id = a.article_id
INNER JOIN
	`article_entity` AS ae ON ae.article_id = a.article_id
INNER JOIN 
	`entity` AS e ON e.entity_id = ae.entity_id
INNER JOIN 
	`entity_type` AS et ON et.entity_type_id = e.entity_type_id
WHERE 
	pa.project_id = 14354
