create schema users;
create schema habits;
create schema observations;
create schema coach;
create schema tracker;

CREATE TABLE users.users (
    id bigint PRIMARY key,
    username character varying(255) UNIQUE NOT NULL,
    email character varying(255) UNIQUE,
    password_hash bytea NOT NULL,
    data jsonb default '{}'::jsonb not null,

    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users.habits (
    id bigint primary key,
    user_id bigint references users.users(id) not null,
    data jsonb default '{}'::jsonb not null,
    
    active boolean default true not null,
    archived boolean DEFAULT false NOT NULL,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE habits.habit_versions (
    id bigint primary key,
    habit_id bigint REFERENCES users.habits(id) not null,
    data jsonb default '{}'::jsonb not null,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE habits.habit_why (
    id bigint PRIMARY KEY,
    user_id bigint REFERENCES users.users(id),
    habit_id bigint REFERENCES users.habits(id),
    why_description text,
    data jsonb default '{}'::jsonb not null,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE observations.observations (
    id bigint primary key,
    user_id bigint references users.users(id),
    observation_name text not null,
    observation_description text,
    data jsonb default '{}'::jsonb not null,
    
    archived boolean DEFAULT false NOT NULL,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE coach.dialogues (
    id bigint PRIMARY KEY,
    user_id bigint REFERENCES users.users(id),
    dialogue_name character varying(255),
    dialogue_version integer,
    dialogue_text text NOT NULL,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE coach.prompts (
    id bigint PRIMARY KEY,
    dialogue_id bigint REFERENCES coach.dialogues(id),
    prompt_text text NOT NULL,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE tracker.daily_tracker (
    id bigint PRIMARY KEY,
    user_id bigint REFERENCES users.users(id),
    track_date date NOT NULL,
    data jsonb default '{}'::jsonb not null,
    notes text,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE tracker.habit_reflections (
    id bigint PRIMARY KEY,
    user_id bigint REFERENCES users.users(id),
    habit_id bigint REFERENCES users.habits(id),
    daily_tracker_id bigint REFERENCES tracker.daily_tracker(id),
    reflection text,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

create sequence users.seq_users_id;
create sequence users.seq_habits_id;
create sequence habits.seq_habit_versions_id;
create sequence habits.seq_habit_why_id;
create sequence observations.seq_observations_id;
create sequence coach.seq_dialogues_id;
create sequence coach.seq_prompts_id;
create sequence tracker.seq_daily_tracker_id;
create sequence tracker.seq_habit_reflections_id;

CREATE INDEX idx_users_habits_on_user_id ON users.habits (user_id);
CREATE INDEX idx_habits_versions_on_habit_id ON habits.habit_versions (habit_id);
CREATE INDEX idx_habits_why_on_user_id ON habits.habit_why (user_id);
CREATE INDEX idx_habits_why_on_habit_id ON habits.habit_why (habit_id);
CREATE INDEX idx_observations_on_user_id ON observations.observations (user_id);
CREATE INDEX idx_coach_dialogues_on_user_id ON coach.dialogues (user_id);
CREATE INDEX idx_tracker_daily_tracker_on_user_id ON tracker.daily_tracker (user_id);
CREATE INDEX idx_tracker_habit_reflections_on_user_id ON tracker.habit_reflections (user_id);
CREATE INDEX idx_tracker_habit_reflections_on_habit_id ON tracker.habit_reflections (habit_id);