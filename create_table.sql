CREATE TABLE Titles (
  title_id 			  VARCHAR(255) NOT NULL, -- not null bc PK
  title_type 			VARCHAR(50),
  primary_title 	TEXT, -- some are really long
  original_title 	TEXT, -- some are really long
  is_adult 			  BOOLEAN,
  start_year			INTEGER, -- add better domain here (>1800)
  end_year 			  INTEGER, -- add better domain here (>0)
  runtime_minutes	INTEGER, -- add better domain here (>0)
  CONSTRAINT Titles_pri_key PRIMARY KEY(title_id)
);

CREATE TABLE Title_ratings (
  title_id 			  VARCHAR(255) NOT NULL, -- not null bc PK
  average_rating	FLOAT,
  num_votes			  INTEGER,
	CONSTRAINT Title_ratings_pri_key PRIMARY KEY (title_id),
	CONSTRAINT Title_ratings_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);

CREATE TABLE Aliases (
  title_id          VARCHAR(255) NOT NULL, -- not null bc PK
  ordering          INTEGER NOT NULL, -- not null bc PK
  title             TEXT NOT NULL,
  region				    CHAR(4),
  language          CHAR(4),
  is_original_title	BOOLEAN,
	CONSTRAINT Aliases_pri_key PRIMARY KEY (title_id,ordering),
	CONSTRAINT Aliases_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);

CREATE TABLE Alias_types (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  ordering			INTEGER NOT NULL, -- not null bc PK
  type				  VARCHAR(255) NOT NULL,-- Only stored if not null
	CONSTRAINT Alias_types_pri_key PRIMARY KEY (title_id,ordering),
	CONSTRAINT Alias_types_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);

CREATE TABLE ALias_attributes (
  title_id			VARCHAR(255) NOT NULL, -- not null bc PK
  ordering			INTEGER NOT NULL, -- not null bc PK
  attribute			VARCHAR(255) NOT NULL, -- only stored if not null
	CONSTRAINT Alias_attributes_pri_key PRIMARY KEY (title_id,ordering),
	CONSTRAINT Alias_attributes_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);

CREATE TABLE Episode_belongs_to (
  episode_title_id          VARCHAR(255) NOT NULL, -- not null bc PK
  parent_tv_show_title_id   VARCHAR(255) NOT NULL,
  season_number             INTEGER,
  episode_number            INTEGER,
	CONSTRAINT Episode_belongs_to_pri_key PRIMARY KEY (episode_title_id),
	CONSTRAINT Episode_belongs_to_ep_title_id_fkey FOREIGN KEY (episode_title_id) REFERENCES Titles(title_id),
	CONSTRAINT Episode_belongs_to_show_title_id_fkey FOREIGN KEY (parent_tv_show_title_id) REFERENCES Titles(title_id)
);

CREATE TABLE Title_genres (
  title_id    VARCHAR(255) NOT NULL, -- not null bc PK
  genre				VARCHAR(255) NOT NULL, -- not null bc PK
	CONSTRAINT Title_genres_pri_key PRIMARY KEY (title_id,genre),
	CONSTRAINT Title_genres_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);

CREATE TABLE Names_ (
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  name_         VARCHAR(255) NOT NULL, -- everybody has a name
  birth_year    SMALLINT, -- add a better domain here
  death_year    SMALLINT, -- add a better domain here
  CONSTRAINT Names_pri_key PRIMARY KEY (name_id)
);

CREATE TABLE Name_worked_as (
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  profession    VARCHAR(255) NOT NULL, -- not null bc PK
	CONSTRAINT Name_worked_as_pri_key PRIMARY KEY (name_id,profession),
	CONSTRAINT Name_worked_as_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id)
);

CREATE TABLE Had_role (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  role_         TEXT NOT NULL, -- not null bc PK
	CONSTRAINT Had_role_pri_key PRIMARY KEY (title_id,name_id,role_),
	CONSTRAINT Had_role_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id),
	CONSTRAINT Had_role_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id)
);

CREATE TABLE Known_for (
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
	CONSTRAINT Known_for_pri_key PRIMARY KEY (name_id,title_id),
	CONSTRAINT Known_for_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id),
	CONSTRAINT Known_for_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);

CREATE TABLE Directors (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
	CONSTRAINT Directors_pri_key PRIMARY KEY (title_id,name_id),
	CONSTRAINT Directors_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id),
	CONSTRAINT Directors_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id)
);

CREATE TABLE Writers (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
	CONSTRAINT Writers_pri_key PRIMARY KEY (title_id,name_id),
	CONSTRAINT Writers_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id),
	CONSTRAINT Writers_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id)
);

CREATE TABLE Principals (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  ordering      SMALLINT NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL,
  job_category  VARCHAR(255),
  job           TEXT,
	CONSTRAINT Principals_pri_key PRIMARY KEY (title_id,ordering),
	CONSTRAINT Principals_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id),
	CONSTRAINT Principals_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id)
);