CREATE TABLE dev.users (
    id uuid DEFAULT dev.uuid_generate_v4() NOT NULL,
    username character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password_hash bytea NOT NULL
);

CREATE TABLE dev.habits (
    id uuid DEFAULT dev.uuid_generate_v4() NOT NULL,
    user_id uuid,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    metadata jsonb NOT NULL,
    active boolean NOT NULL,
    archived boolean DEFAULT false NOT NULL
);

CREATE TABLE dev.habit_versions (
    id uuid DEFAULT dev.uuid_generate_v4() NOT NULL,
    habit_id uuid REFERENCES dev.habits(id),
    version_description text NOT NULL,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    metadata jsonb NOT NULL
);

CREATE TABLE dev.observations (
    id uuid DEFAULT dev.uuid_generate_v4() NOT NULL,
    user_id uuid,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    metadata jsonb NOT NULL,
    archived boolean DEFAULT false NOT NULL
);

CREATE TABLE dev.responses (
    id uuid DEFAULT dev.uuid_generate_v4() NOT NULL,
    user_id uuid,
    ref_id uuid,  -- This can reference either habits or observations based on type
    type text CHECK(type IN ('habit', 'observation')),  -- Enum type for either habit or observation
    date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    metadata jsonb NOT NULL
);