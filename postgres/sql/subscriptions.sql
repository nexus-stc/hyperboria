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

root@postgres-master-0:/# pg_dump -t 'subscriptions' --schema-only idm
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
-- Name: subscriptions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subscriptions (
    id bigint DEFAULT nextval('public.subscriptions_id_seq'::regclass) NOT NULL,
    chat_id bigint NOT NULL,
    subscription_query text NOT NULL,
    schedule text NOT NULL,
    is_oneshot boolean DEFAULT false NOT NULL,
    is_downloadable boolean DEFAULT false NOT NULL,
    created_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    updated_at integer DEFAULT date_part('epoch'::text, now()) NOT NULL,
    valid_until integer DEFAULT 2147483647 NOT NULL,
    next_check_at integer NOT NULL,
    subscription_type integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.subscriptions OWNER TO postgres;

--
-- Name: subscriptions_chat_id_subscription_query_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX subscriptions_chat_id_subscription_query_idx ON public.subscriptions USING btree (chat_id, subscription_query);


--
-- Name: subscriptions_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX subscriptions_id_idx ON public.subscriptions USING btree (id);


--
-- Name: subscriptions_next_check_at_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX subscriptions_next_check_at_idx ON public.subscriptions USING btree (next_check_at);


--
-- Name: subscriptions_subscription_query_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX subscriptions_subscription_query_idx ON public.subscriptions USING btree (subscription_query);


--
-- Name: subscriptions set_timestamp_on_subscriptions; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER set_timestamp_on_subscriptions BEFORE UPDATE ON public.subscriptions FOR EACH ROW EXECUTE FUNCTION public.trigger_set_updated_at();


--
-- Name: TABLE subscriptions; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.subscriptions TO idm_api;


--
-- PostgreSQL database dump complete
--