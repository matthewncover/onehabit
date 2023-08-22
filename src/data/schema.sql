create extension if not exists "uuid-ossp";

create table users(
    user_id uuid primary key default uuid_generate_v4(),
    username varchar(255) unique not null,
    user_email varchar(255) unique not null,
    password_hash bytea not null
);

create table goals (
    goal_id uuid default uuid_generate_v4(),
    goal_version text not null,
    user_id uuid references users(user_id),
    created_date timestamp not null default current_timestamp,
    goal jsonb not null,
    active boolean not null,
    primary key (goal_id, goal_version)
);

create table responses (
    response_id uuid primary key default uuid_generate_v4(),
    user_id uuid references users(user_id),
    response_date timestamp not null default current_timestamp,
    response jsonb not null
);