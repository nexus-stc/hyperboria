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
-- Name: cross_references; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cross_references (
    source_id bigint NOT NULL,
    target_id bigint NOT NULL
);


--
-- Name: cross_references cross_references_source_id_target_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cross_references
    ADD CONSTRAINT cross_references_source_id_target_id_key UNIQUE (source_id, target_id);


--
-- PostgreSQL database dump complete
--
