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
-- Name: scitech; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scitech (
    id bigint DEFAULT nextval('public.documents_id_seq'::regclass) NOT NULL,
    cu text,
    cu_suf character varying(1),
    description text,
    doi character varying(512),
    edition character varying(64),
    extension character varying(8),
    fiction_id bigint,
    filesize bigint,
    is_deleted boolean DEFAULT false NOT NULL,
    isbns text[],
    language text,
    libgen_id bigint,
    meta_language text,
    md5 uuid NOT NULL,
    pages integer,
    series text,
    tags text[],
    title text,
    updated_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    original_id bigint,
    volume text,
    authors text[],
    issued_at bigint,
    ipfs_multihashes text[]
);


--
-- Name: scitech scitech_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scitech
    ADD CONSTRAINT scitech_pkey PRIMARY KEY (id);


--
-- Name: scitech_doi_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX scitech_doi_idx ON public.scitech USING btree (doi);


--
-- Name: scitech_fiction_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX scitech_fiction_id_idx ON public.scitech USING btree (fiction_id);


--
-- Name: scitech_isbn_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX scitech_isbn_idx ON public.scitech USING gin (isbns);


--
-- Name: scitech_libgen_id_doi_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX scitech_libgen_id_doi_idx ON public.scitech USING btree (libgen_id, doi);


--
-- Name: scitech_libgen_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX scitech_libgen_id_idx ON public.scitech USING btree (libgen_id);


--
-- Name: scitech_md5_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX scitech_md5_idx ON public.scitech USING btree (md5);


--
-- Name: scitech_original_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX scitech_original_id_idx ON public.scitech USING btree (original_id);


--
-- Name: scitech set_timestamp_on_scitech; Type: TRIGGER; Schema: public; Owner: -
--

CREATE TRIGGER set_timestamp_on_scitech BEFORE UPDATE ON public.scitech FOR EACH ROW EXECUTE FUNCTION public.trigger_set_updated_at();


--
-- PostgreSQL database dump complete
--
