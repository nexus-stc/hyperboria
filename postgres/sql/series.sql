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
-- Name: series; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.series (
    id bigint,
    issns text[],
    name text
);


ALTER TABLE public.series OWNER TO postgres;

--
-- Name: series_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.series_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.series_id_seq OWNER TO postgres;

--
-- Name: series_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.series_id_seq OWNED BY public.series.id;


--
-- Name: series id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.series ALTER COLUMN id SET DEFAULT nextval('public.series_id_seq'::regclass);


--
-- Name: series_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX series_id_idx ON public.series USING btree (id);


--
-- Name: series_issns_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX series_issns_idx ON public.series USING gin (issns);


--
-- Name: TABLE series; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.series TO nexus_api;


--
-- PostgreSQL database dump complete
--
