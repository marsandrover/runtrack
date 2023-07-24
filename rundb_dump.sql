--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

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
-- Name: runs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.runs (
    std_id integer NOT NULL,
    std_distance character varying(240) NOT NULL,
    std_duration character varying(240) NOT NULL,
    date character varying(240) NOT NULL
);


ALTER TABLE public.runs OWNER TO postgres;

--
-- Data for Name: runs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.runs (std_id, std_distance, std_duration, date) FROM stdin;
1	5k	31:29	1/05/2020
3	5k	29:59	15/05/2020
2	5k	30:29	10/05/2020
\.


--
-- Name: runs runs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.runs
    ADD CONSTRAINT runs_pkey PRIMARY KEY (std_id);


--
-- PostgreSQL database dump complete
--

