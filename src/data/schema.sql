create table users(
    user_id uuid unique not null,
    username varchar(255) unique not null,
    user_email varchar(255) unique not null
);

create table goals (
    goal_id uuid unique not null,
    goal_version text not null,
    user_id uuid references users(user_id),
    created_date date not null,
    goal JSON not null,
    active bool not null
);

create table responses (
    response_id uuid unique not null,
    user_id uuid references users(user_id),
    response_date date not null,
    response JSON not null,
);