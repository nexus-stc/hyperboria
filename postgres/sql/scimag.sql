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
-- Name: scimag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scimag (
    id bigint DEFAULT nextval('public.documents_id_seq'::regclass) NOT NULL,
    abstract text,
    doi character varying(512),
    filesize integer,
    first_page integer,
    is_deleted boolean DEFAULT false NOT NULL,
    issue text,
    container_title text,
    journal_id integer,
    language text,
    last_page integer,
    meta_language text,
    md5 uuid,
    tags text[],
    telegram_file_id text,
    title text,
    updated_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    volume text,
    embedding bytea,
    ref_by_count integer,
    scimag_bulk_id integer,
    issns text[],
    authors text[],
    issued_at bigint,
    type text,
    ipfs_multihashes text[]
);


--
-- Name: scimag scimag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scimag
    ADD CONSTRAINT scimag_pkey PRIMARY KEY (id);


--
-- Name: scimag_doi_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX scimag_doi_idx ON public.scimag USING btree (doi);


--
-- Name: scimag_md5_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX scimag_md5_idx ON public.scimag USING btree (md5);


--
-- Name: scimag_telegram_file_id_not_null_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX scimag_telegram_file_id_not_null_idx ON public.scimag USING btree (telegram_file_id) WHERE (telegram_file_id IS NOT NULL);


--
-- Name: scimag set_timestamp_on_scimag; Type: TRIGGER; Schema: public; Owner: -
--

CREATE TRIGGER set_timestamp_on_scimag BEFORE UPDATE ON public.scimag FOR EACH ROW EXECUTE FUNCTION public.trigger_set_updated_at();


--
-- PostgreSQL database dump complete
--
