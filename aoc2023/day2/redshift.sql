WITH

source AS(
  SELECT * FROM develop.puzzle_input_2
)

, numbers AS (
  SELECT number as idx FROM develop.dim_numbers ORDER BY 1 LIMIT 500
)

, games_round AS(
  SELECT
    TRIM(REPLACE(SPLIT_PART(t.games, ':', 1), 'Game ', ''))::INT AS game_idx,
    TRIM(SPLIT_PART(t.games, ':',2)) AS game_rounds,
    LENGTH(REGEXP_REPLACE( game_rounds, '[^;]', '') + 1) AS number_of_round
  FROM source t
)

, game_results AS (
  SELECT
    t.*,
    TRIM(SPLIT_PART(t.game_rounds, ';', n.idx)) AS individual_round,
    CASE
      WHEN individual_round ilike '%red%' THEN REGEXP_REPLACE(REGEXP_SUBSTR(individual_round, '\\d+ red'), '\\D+', '')::INT
    END AS red,
    CASE
      WHEN individual_round ilike '%green%' THEN REGEXP_REPLACE(REGEXP_SUBSTR(individual_round, '\\d+ green'), '\\D+', '')::INT
    END AS green,
    CASE
      WHEN individual_round ilike '%blue%' THEN REGEXP_REPLACE(REGEXP_SUBSTR(individual_round, '\\d+ blue'), '\\D+', '')::INT
    END AS blue
  FROM games_round t
  LEFT JOIN numbers n ON split_part(t.game_rounds, ';', n.idx::INT) <> ''
)

, max_value AS (
  SELECT
    game_idx,
    game_rounds,
    MAX(red)::INT AS red,
    MAX(green)::INT AS green,
    MAX(blue)::INT AS blue
  FROM game_results
  GROUP BY 1,2
)

SELECT
  SUM(CASE WHEN red <= 12 AND green <= 13 AND blue <= 14 THEN game_idx END) AS puzzle_1_result,
  SUM(red * green * blue) AS puzzle_2_result
FROM max_value
;