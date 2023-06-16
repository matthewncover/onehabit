CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    user_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TYPE answer_type AS ENUM ('bool', 'dropdown', 'freeform', 'numeric');

CREATE TABLE questions (
    question_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer_type answer_type NOT NULL,
    created_date DATE NOT NULL
);

CREATE TABLE responses (
    response_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    question_id UUID REFERENCES questions(question_id),
    response TEXT,
    response_date DATE NOT NULL
);