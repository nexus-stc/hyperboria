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
-- Name: votes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.votes (
    document_id bigint NOT NULL,
    value integer NOT NULL,
    voter_id bigint NOT NULL
);


--
-- Name: votes_document_id_voter_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX votes_document_id_voter_id_idx ON public.votes USING btree (document_id, voter_id);


--
-- PostgreSQL database dump complete
--
