create table if not exists memories (
    id uuid primary key default gen_random_uuid(),
    content text not null,
    memory_type text default 'episodic',
    embedding jsonb,
    created_at timestamptz default now(),
    metadata jsonb default '{}'::jsonb
);

create index if not exists memories_created_at_idx
on memories(created_at desc);
