-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
player_id serial primary key,
player_name text
);

CREATE TABLE matches(
match_id serial primary key,
winner_id integer references players(player_id),
loser_id integer references players(player_id)
);

CREATE VIEW win_view AS 
    SELECT players.player_id, COUNT(matches.winner_id) AS win_num 
    FROM players LEFT JOIN matches ON players.player_id = matches.winner_id
    GROUP BY players.player_id;

CREATE VIEW loss_view AS
    SELECT players.player_id, COUNT(matches.loser_id) AS loss_num
    FROM players LEFT JOIN matches ON players.player_id = matches.loser_id
    GROUP BY players.player_id;
