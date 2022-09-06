--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

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
-- Name: scitech; Type: TABLE; Schema: public; Owner: postgres
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
    ipfs_multihashes text[],
    created_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    periodical text
);


ALTER TABLE public.scitech OWNER TO postgres;

--
-- Name: scitech_doi_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX scitech_doi_idx ON public.scitech USING btree (doi);


--
-- Name: scitech_fiction_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX scitech_fiction_id_idx ON public.scitech USING btree (fiction_id);


--
-- Name: scitech_isbn_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX scitech_isbn_idx ON public.scitech USING gin (isbns);


--
-- Name: scitech_libgen_id_doi_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX scitech_libgen_id_doi_idx ON public.scitech USING btree (libgen_id, doi);


--
-- Name: scitech_libgen_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX scitech_libgen_id_idx ON public.scitech USING btree (libgen_id);


--
-- Name: scitech_md5_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX scitech_md5_idx ON public.scitech USING btree (md5);


--
-- Name: scitech_original_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX scitech_original_id_idx ON public.scitech USING btree (original_id);


--
-- Name: scitech_pkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX scitech_pkey ON public.scitech USING btree (id);


--
-- Name: scitech set_timestamp_on_scitech; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER set_timestamp_on_scitech BEFORE UPDATE ON public.scitech FOR EACH ROW EXECUTE FUNCTION public.trigger_set_updated_at();


--
-- Name: TABLE scitech; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.scitech TO nexus_pipe;
GRANT SELECT,UPDATE ON TABLE public.scitech TO nexus_api;


--
-- PostgreSQL database dump complete
--