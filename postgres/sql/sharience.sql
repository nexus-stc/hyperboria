--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Debian 13.2-1.pgdg100+1)
-- Dumped by pg_dump version 13.2 (Debian 13.2-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: sharience; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sharience (
    id bigint DEFAULT nextval('public.documents_id_seq'::regclass) NOT NULL,
    parent_id bigint NOT NULL,
    uploader_id bigint NOT NULL,
    created_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    updated_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    md5 uuid,
    filesize integer,
    ipfs_multihashes text[]
);


ALTER TABLE public.sharience OWNER TO postgres;

--
-- Name: sharience sharience_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sharience
    ADD CONSTRAINT sharience_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--
