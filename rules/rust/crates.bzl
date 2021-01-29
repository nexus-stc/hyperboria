"""
@generated
cargo-raze generated Bazel file.

DO NOT EDIT! Replaced on runs of cargo-raze
"""

load("@bazel_tools//tools/build_defs/repo:git.bzl", "new_git_repository")  # buildifier: disable=load
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")  # buildifier: disable=load
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")  # buildifier: disable=load

def raze_fetch_remote_crates():
    """This function defines a collection of repos and should be called in a WORKSPACE file"""
    maybe(
        http_archive,
        name = "raze__actix__0_10_0",
        url = "https://crates.io/api/v1/crates/actix/0.10.0/download",
        type = "tar.gz",
        strip_prefix = "actix-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_codec__0_2_0",
        url = "https://crates.io/api/v1/crates/actix-codec/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "actix-codec-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-codec-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_codec__0_3_0",
        url = "https://crates.io/api/v1/crates/actix-codec/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "actix-codec-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-codec-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_connect__2_0_0",
        url = "https://crates.io/api/v1/crates/actix-connect/2.0.0/download",
        type = "tar.gz",
        strip_prefix = "actix-connect-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-connect-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_cors__0_5_4",
        url = "https://crates.io/api/v1/crates/actix-cors/0.5.4/download",
        type = "tar.gz",
        strip_prefix = "actix-cors-0.5.4",
        build_file = Label("//rules/rust/remote:BUILD.actix-cors-0.5.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_http__2_2_0",
        url = "https://crates.io/api/v1/crates/actix-http/2.2.0/download",
        type = "tar.gz",
        strip_prefix = "actix-http-2.2.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-http-2.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_macros__0_1_3",
        url = "https://crates.io/api/v1/crates/actix-macros/0.1.3/download",
        type = "tar.gz",
        strip_prefix = "actix-macros-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.actix-macros-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_router__0_2_6",
        url = "https://crates.io/api/v1/crates/actix-router/0.2.6/download",
        type = "tar.gz",
        strip_prefix = "actix-router-0.2.6",
        build_file = Label("//rules/rust/remote:BUILD.actix-router-0.2.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_rt__1_1_1",
        url = "https://crates.io/api/v1/crates/actix-rt/1.1.1/download",
        type = "tar.gz",
        strip_prefix = "actix-rt-1.1.1",
        build_file = Label("//rules/rust/remote:BUILD.actix-rt-1.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_server__1_0_4",
        url = "https://crates.io/api/v1/crates/actix-server/1.0.4/download",
        type = "tar.gz",
        strip_prefix = "actix-server-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.actix-server-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_service__1_0_6",
        url = "https://crates.io/api/v1/crates/actix-service/1.0.6/download",
        type = "tar.gz",
        strip_prefix = "actix-service-1.0.6",
        build_file = Label("//rules/rust/remote:BUILD.actix-service-1.0.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_testing__1_0_1",
        url = "https://crates.io/api/v1/crates/actix-testing/1.0.1/download",
        type = "tar.gz",
        strip_prefix = "actix-testing-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.actix-testing-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_threadpool__0_3_3",
        url = "https://crates.io/api/v1/crates/actix-threadpool/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "actix-threadpool-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.actix-threadpool-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_tls__2_0_0",
        url = "https://crates.io/api/v1/crates/actix-tls/2.0.0/download",
        type = "tar.gz",
        strip_prefix = "actix-tls-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-tls-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_utils__1_0_6",
        url = "https://crates.io/api/v1/crates/actix-utils/1.0.6/download",
        type = "tar.gz",
        strip_prefix = "actix-utils-1.0.6",
        build_file = Label("//rules/rust/remote:BUILD.actix-utils-1.0.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_utils__2_0_0",
        url = "https://crates.io/api/v1/crates/actix-utils/2.0.0/download",
        type = "tar.gz",
        strip_prefix = "actix-utils-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-utils-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_web__3_3_2",
        url = "https://crates.io/api/v1/crates/actix-web/3.3.2/download",
        type = "tar.gz",
        strip_prefix = "actix-web-3.3.2",
        build_file = Label("//rules/rust/remote:BUILD.actix-web-3.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_web_codegen__0_4_0",
        url = "https://crates.io/api/v1/crates/actix-web-codegen/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "actix-web-codegen-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-web-codegen-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_derive__0_5_0",
        url = "https://crates.io/api/v1/crates/actix_derive/0.5.0/download",
        type = "tar.gz",
        strip_prefix = "actix_derive-0.5.0",
        build_file = Label("//rules/rust/remote:BUILD.actix_derive-0.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__addr2line__0_14_1",
        url = "https://crates.io/api/v1/crates/addr2line/0.14.1/download",
        type = "tar.gz",
        strip_prefix = "addr2line-0.14.1",
        build_file = Label("//rules/rust/remote:BUILD.addr2line-0.14.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__adler__0_2_3",
        url = "https://crates.io/api/v1/crates/adler/0.2.3/download",
        type = "tar.gz",
        strip_prefix = "adler-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.adler-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ahash__0_4_7",
        url = "https://crates.io/api/v1/crates/ahash/0.4.7/download",
        type = "tar.gz",
        strip_prefix = "ahash-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.ahash-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__aho_corasick__0_7_15",
        url = "https://crates.io/api/v1/crates/aho-corasick/0.7.15/download",
        type = "tar.gz",
        strip_prefix = "aho-corasick-0.7.15",
        build_file = Label("//rules/rust/remote:BUILD.aho-corasick-0.7.15.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__alloc_no_stdlib__2_0_1",
        url = "https://crates.io/api/v1/crates/alloc-no-stdlib/2.0.1/download",
        type = "tar.gz",
        strip_prefix = "alloc-no-stdlib-2.0.1",
        build_file = Label("//rules/rust/remote:BUILD.alloc-no-stdlib-2.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__alloc_stdlib__0_2_1",
        url = "https://crates.io/api/v1/crates/alloc-stdlib/0.2.1/download",
        type = "tar.gz",
        strip_prefix = "alloc-stdlib-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.alloc-stdlib-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ansi_term__0_11_0",
        url = "https://crates.io/api/v1/crates/ansi_term/0.11.0/download",
        type = "tar.gz",
        strip_prefix = "ansi_term-0.11.0",
        build_file = Label("//rules/rust/remote:BUILD.ansi_term-0.11.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__antidote__1_0_0",
        url = "https://crates.io/api/v1/crates/antidote/1.0.0/download",
        type = "tar.gz",
        strip_prefix = "antidote-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.antidote-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arc_swap__0_4_8",
        url = "https://crates.io/api/v1/crates/arc-swap/0.4.8/download",
        type = "tar.gz",
        strip_prefix = "arc-swap-0.4.8",
        build_file = Label("//rules/rust/remote:BUILD.arc-swap-0.4.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arc_swap__1_2_0",
        url = "https://crates.io/api/v1/crates/arc-swap/1.2.0/download",
        type = "tar.gz",
        strip_prefix = "arc-swap-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.arc-swap-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arrayref__0_3_6",
        url = "https://crates.io/api/v1/crates/arrayref/0.3.6/download",
        type = "tar.gz",
        strip_prefix = "arrayref-0.3.6",
        build_file = Label("//rules/rust/remote:BUILD.arrayref-0.3.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arrayvec__0_5_2",
        url = "https://crates.io/api/v1/crates/arrayvec/0.5.2/download",
        type = "tar.gz",
        strip_prefix = "arrayvec-0.5.2",
        build_file = Label("//rules/rust/remote:BUILD.arrayvec-0.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__async_trait__0_1_42",
        url = "https://crates.io/api/v1/crates/async-trait/0.1.42/download",
        type = "tar.gz",
        strip_prefix = "async-trait-0.1.42",
        build_file = Label("//rules/rust/remote:BUILD.async-trait-0.1.42.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__atomicwrites__0_2_5",
        url = "https://crates.io/api/v1/crates/atomicwrites/0.2.5/download",
        type = "tar.gz",
        strip_prefix = "atomicwrites-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.atomicwrites-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__atty__0_2_14",
        url = "https://crates.io/api/v1/crates/atty/0.2.14/download",
        type = "tar.gz",
        strip_prefix = "atty-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.atty-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__autocfg__1_0_1",
        url = "https://crates.io/api/v1/crates/autocfg/1.0.1/download",
        type = "tar.gz",
        strip_prefix = "autocfg-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.autocfg-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__awc__2_0_3",
        url = "https://crates.io/api/v1/crates/awc/2.0.3/download",
        type = "tar.gz",
        strip_prefix = "awc-2.0.3",
        build_file = Label("//rules/rust/remote:BUILD.awc-2.0.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__backtrace__0_3_55",
        url = "https://crates.io/api/v1/crates/backtrace/0.3.55/download",
        type = "tar.gz",
        strip_prefix = "backtrace-0.3.55",
        build_file = Label("//rules/rust/remote:BUILD.backtrace-0.3.55.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base_x__0_2_8",
        url = "https://crates.io/api/v1/crates/base-x/0.2.8/download",
        type = "tar.gz",
        strip_prefix = "base-x-0.2.8",
        build_file = Label("//rules/rust/remote:BUILD.base-x-0.2.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_12_3",
        url = "https://crates.io/api/v1/crates/base64/0.12.3/download",
        type = "tar.gz",
        strip_prefix = "base64-0.12.3",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.12.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_13_0",
        url = "https://crates.io/api/v1/crates/base64/0.13.0/download",
        type = "tar.gz",
        strip_prefix = "base64-0.13.0",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_9_3",
        url = "https://crates.io/api/v1/crates/base64/0.9.3/download",
        type = "tar.gz",
        strip_prefix = "base64-0.9.3",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.9.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bb8__0_4_2",
        url = "https://crates.io/api/v1/crates/bb8/0.4.2/download",
        type = "tar.gz",
        strip_prefix = "bb8-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.bb8-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bb8_postgres__0_4_0",
        url = "https://crates.io/api/v1/crates/bb8-postgres/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "bb8-postgres-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.bb8-postgres-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bincode__1_3_1",
        url = "https://crates.io/api/v1/crates/bincode/1.3.1/download",
        type = "tar.gz",
        strip_prefix = "bincode-1.3.1",
        build_file = Label("//rules/rust/remote:BUILD.bincode-1.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bit_set__0_5_2",
        url = "https://crates.io/api/v1/crates/bit-set/0.5.2/download",
        type = "tar.gz",
        strip_prefix = "bit-set-0.5.2",
        build_file = Label("//rules/rust/remote:BUILD.bit-set-0.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bit_vec__0_6_3",
        url = "https://crates.io/api/v1/crates/bit-vec/0.6.3/download",
        type = "tar.gz",
        strip_prefix = "bit-vec-0.6.3",
        build_file = Label("//rules/rust/remote:BUILD.bit-vec-0.6.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bitflags__1_2_1",
        url = "https://crates.io/api/v1/crates/bitflags/1.2.1/download",
        type = "tar.gz",
        strip_prefix = "bitflags-1.2.1",
        build_file = Label("//rules/rust/remote:BUILD.bitflags-1.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bitpacking__0_8_2",
        url = "https://crates.io/api/v1/crates/bitpacking/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "bitpacking-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.bitpacking-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__blake2b_simd__0_5_11",
        url = "https://crates.io/api/v1/crates/blake2b_simd/0.5.11/download",
        type = "tar.gz",
        strip_prefix = "blake2b_simd-0.5.11",
        build_file = Label("//rules/rust/remote:BUILD.blake2b_simd-0.5.11.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__block_buffer__0_9_0",
        url = "https://crates.io/api/v1/crates/block-buffer/0.9.0/download",
        type = "tar.gz",
        strip_prefix = "block-buffer-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.block-buffer-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__brotli__3_3_0",
        url = "https://crates.io/api/v1/crates/brotli/3.3.0/download",
        type = "tar.gz",
        strip_prefix = "brotli-3.3.0",
        build_file = Label("//rules/rust/remote:BUILD.brotli-3.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__brotli_decompressor__2_3_1",
        url = "https://crates.io/api/v1/crates/brotli-decompressor/2.3.1/download",
        type = "tar.gz",
        strip_prefix = "brotli-decompressor-2.3.1",
        build_file = Label("//rules/rust/remote:BUILD.brotli-decompressor-2.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bstr__0_2_14",
        url = "https://crates.io/api/v1/crates/bstr/0.2.14/download",
        type = "tar.gz",
        strip_prefix = "bstr-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.bstr-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bumpalo__3_4_0",
        url = "https://crates.io/api/v1/crates/bumpalo/3.4.0/download",
        type = "tar.gz",
        strip_prefix = "bumpalo-3.4.0",
        build_file = Label("//rules/rust/remote:BUILD.bumpalo-3.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__byteorder__1_4_2",
        url = "https://crates.io/api/v1/crates/byteorder/1.4.2/download",
        type = "tar.gz",
        strip_prefix = "byteorder-1.4.2",
        build_file = Label("//rules/rust/remote:BUILD.byteorder-1.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytes__0_5_6",
        url = "https://crates.io/api/v1/crates/bytes/0.5.6/download",
        type = "tar.gz",
        strip_prefix = "bytes-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.bytes-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytes__1_0_1",
        url = "https://crates.io/api/v1/crates/bytes/1.0.1/download",
        type = "tar.gz",
        strip_prefix = "bytes-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.bytes-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytestring__1_0_0",
        url = "https://crates.io/api/v1/crates/bytestring/1.0.0/download",
        type = "tar.gz",
        strip_prefix = "bytestring-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.bytestring-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cast__0_2_3",
        url = "https://crates.io/api/v1/crates/cast/0.2.3/download",
        type = "tar.gz",
        strip_prefix = "cast-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.cast-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cc__1_0_66",
        url = "https://crates.io/api/v1/crates/cc/1.0.66/download",
        type = "tar.gz",
        strip_prefix = "cc-1.0.66",
        build_file = Label("//rules/rust/remote:BUILD.cc-1.0.66.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__census__0_4_0",
        url = "https://crates.io/api/v1/crates/census/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "census-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.census-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cfg_if__0_1_10",
        url = "https://crates.io/api/v1/crates/cfg-if/0.1.10/download",
        type = "tar.gz",
        strip_prefix = "cfg-if-0.1.10",
        build_file = Label("//rules/rust/remote:BUILD.cfg-if-0.1.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cfg_if__1_0_0",
        url = "https://crates.io/api/v1/crates/cfg-if/1.0.0/download",
        type = "tar.gz",
        strip_prefix = "cfg-if-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.cfg-if-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__chrono__0_4_19",
        url = "https://crates.io/api/v1/crates/chrono/0.4.19/download",
        type = "tar.gz",
        strip_prefix = "chrono-0.4.19",
        build_file = Label("//rules/rust/remote:BUILD.chrono-0.4.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__clap__2_33_3",
        url = "https://crates.io/api/v1/crates/clap/2.33.3/download",
        type = "tar.gz",
        strip_prefix = "clap-2.33.3",
        build_file = Label("//rules/rust/remote:BUILD.clap-2.33.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cloudabi__0_0_3",
        url = "https://crates.io/api/v1/crates/cloudabi/0.0.3/download",
        type = "tar.gz",
        strip_prefix = "cloudabi-0.0.3",
        build_file = Label("//rules/rust/remote:BUILD.cloudabi-0.0.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__colored__2_0_0",
        url = "https://crates.io/api/v1/crates/colored/2.0.0/download",
        type = "tar.gz",
        strip_prefix = "colored-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.colored-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__combine__4_5_2",
        url = "https://crates.io/api/v1/crates/combine/4.5.2/download",
        type = "tar.gz",
        strip_prefix = "combine-4.5.2",
        build_file = Label("//rules/rust/remote:BUILD.combine-4.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__config__0_10_1",
        url = "https://crates.io/api/v1/crates/config/0.10.1/download",
        type = "tar.gz",
        strip_prefix = "config-0.10.1",
        build_file = Label("//rules/rust/remote:BUILD.config-0.10.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__const_fn__0_4_5",
        url = "https://crates.io/api/v1/crates/const_fn/0.4.5/download",
        type = "tar.gz",
        strip_prefix = "const_fn-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.const_fn-0.4.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__constant_time_eq__0_1_5",
        url = "https://crates.io/api/v1/crates/constant_time_eq/0.1.5/download",
        type = "tar.gz",
        strip_prefix = "constant_time_eq-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.constant_time_eq-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cookie__0_14_3",
        url = "https://crates.io/api/v1/crates/cookie/0.14.3/download",
        type = "tar.gz",
        strip_prefix = "cookie-0.14.3",
        build_file = Label("//rules/rust/remote:BUILD.cookie-0.14.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__copyless__0_1_5",
        url = "https://crates.io/api/v1/crates/copyless/0.1.5/download",
        type = "tar.gz",
        strip_prefix = "copyless-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.copyless-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cpuid_bool__0_1_2",
        url = "https://crates.io/api/v1/crates/cpuid-bool/0.1.2/download",
        type = "tar.gz",
        strip_prefix = "cpuid-bool-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.cpuid-bool-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crc32fast__1_2_1",
        url = "https://crates.io/api/v1/crates/crc32fast/1.2.1/download",
        type = "tar.gz",
        strip_prefix = "crc32fast-1.2.1",
        build_file = Label("//rules/rust/remote:BUILD.crc32fast-1.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__criterion__0_3_3",
        url = "https://crates.io/api/v1/crates/criterion/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "criterion-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.criterion-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__criterion_plot__0_4_3",
        url = "https://crates.io/api/v1/crates/criterion-plot/0.4.3/download",
        type = "tar.gz",
        strip_prefix = "criterion-plot-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.criterion-plot-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam__0_7_3",
        url = "https://crates.io/api/v1/crates/crossbeam/0.7.3/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_channel__0_4_4",
        url = "https://crates.io/api/v1/crates/crossbeam-channel/0.4.4/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-channel-0.4.4",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-channel-0.4.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_channel__0_5_0",
        url = "https://crates.io/api/v1/crates/crossbeam-channel/0.5.0/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-channel-0.5.0",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-channel-0.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_deque__0_7_3",
        url = "https://crates.io/api/v1/crates/crossbeam-deque/0.7.3/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-deque-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-deque-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_deque__0_8_0",
        url = "https://crates.io/api/v1/crates/crossbeam-deque/0.8.0/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-deque-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-deque-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_epoch__0_8_2",
        url = "https://crates.io/api/v1/crates/crossbeam-epoch/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-epoch-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-epoch-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_epoch__0_9_1",
        url = "https://crates.io/api/v1/crates/crossbeam-epoch/0.9.1/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-epoch-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-epoch-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_queue__0_2_3",
        url = "https://crates.io/api/v1/crates/crossbeam-queue/0.2.3/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-queue-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-queue-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_utils__0_7_2",
        url = "https://crates.io/api/v1/crates/crossbeam-utils/0.7.2/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-utils-0.7.2",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-utils-0.7.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_utils__0_8_1",
        url = "https://crates.io/api/v1/crates/crossbeam-utils/0.8.1/download",
        type = "tar.gz",
        strip_prefix = "crossbeam-utils-0.8.1",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-utils-0.8.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crunchy__0_2_2",
        url = "https://crates.io/api/v1/crates/crunchy/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "crunchy-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.crunchy-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crypto_mac__0_10_0",
        url = "https://crates.io/api/v1/crates/crypto-mac/0.10.0/download",
        type = "tar.gz",
        strip_prefix = "crypto-mac-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.crypto-mac-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crypto_mac__0_9_1",
        url = "https://crates.io/api/v1/crates/crypto-mac/0.9.1/download",
        type = "tar.gz",
        strip_prefix = "crypto-mac-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.crypto-mac-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__csv__1_1_5",
        url = "https://crates.io/api/v1/crates/csv/1.1.5/download",
        type = "tar.gz",
        strip_prefix = "csv-1.1.5",
        build_file = Label("//rules/rust/remote:BUILD.csv-1.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__csv_core__0_1_10",
        url = "https://crates.io/api/v1/crates/csv-core/0.1.10/download",
        type = "tar.gz",
        strip_prefix = "csv-core-0.1.10",
        build_file = Label("//rules/rust/remote:BUILD.csv-core-0.1.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__deadpool__0_5_2",
        url = "https://crates.io/api/v1/crates/deadpool/0.5.2/download",
        type = "tar.gz",
        strip_prefix = "deadpool-0.5.2",
        build_file = Label("//rules/rust/remote:BUILD.deadpool-0.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__deadpool_postgres__0_5_6",
        url = "https://crates.io/api/v1/crates/deadpool-postgres/0.5.6/download",
        type = "tar.gz",
        strip_prefix = "deadpool-postgres-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.deadpool-postgres-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__derive_more__0_99_11",
        url = "https://crates.io/api/v1/crates/derive_more/0.99.11/download",
        type = "tar.gz",
        strip_prefix = "derive_more-0.99.11",
        build_file = Label("//rules/rust/remote:BUILD.derive_more-0.99.11.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__digest__0_9_0",
        url = "https://crates.io/api/v1/crates/digest/0.9.0/download",
        type = "tar.gz",
        strip_prefix = "digest-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.digest-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dirs__2_0_2",
        url = "https://crates.io/api/v1/crates/dirs/2.0.2/download",
        type = "tar.gz",
        strip_prefix = "dirs-2.0.2",
        build_file = Label("//rules/rust/remote:BUILD.dirs-2.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dirs_sys__0_3_5",
        url = "https://crates.io/api/v1/crates/dirs-sys/0.3.5/download",
        type = "tar.gz",
        strip_prefix = "dirs-sys-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.dirs-sys-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__discard__1_0_4",
        url = "https://crates.io/api/v1/crates/discard/1.0.4/download",
        type = "tar.gz",
        strip_prefix = "discard-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.discard-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dotenv__0_15_0",
        url = "https://crates.io/api/v1/crates/dotenv/0.15.0/download",
        type = "tar.gz",
        strip_prefix = "dotenv-0.15.0",
        build_file = Label("//rules/rust/remote:BUILD.dotenv-0.15.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__downcast_rs__1_2_0",
        url = "https://crates.io/api/v1/crates/downcast-rs/1.2.0/download",
        type = "tar.gz",
        strip_prefix = "downcast-rs-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.downcast-rs-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dtoa__0_4_7",
        url = "https://crates.io/api/v1/crates/dtoa/0.4.7/download",
        type = "tar.gz",
        strip_prefix = "dtoa-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.dtoa-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__either__1_6_1",
        url = "https://crates.io/api/v1/crates/either/1.6.1/download",
        type = "tar.gz",
        strip_prefix = "either-1.6.1",
        build_file = Label("//rules/rust/remote:BUILD.either-1.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__encoding_rs__0_8_26",
        url = "https://crates.io/api/v1/crates/encoding_rs/0.8.26/download",
        type = "tar.gz",
        strip_prefix = "encoding_rs-0.8.26",
        build_file = Label("//rules/rust/remote:BUILD.encoding_rs-0.8.26.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__enum_as_inner__0_3_3",
        url = "https://crates.io/api/v1/crates/enum-as-inner/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "enum-as-inner-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.enum-as-inner-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__env_logger__0_8_2",
        url = "https://crates.io/api/v1/crates/env_logger/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "env_logger-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.env_logger-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__erased_serde__0_3_13",
        url = "https://crates.io/api/v1/crates/erased-serde/0.3.13/download",
        type = "tar.gz",
        strip_prefix = "erased-serde-0.3.13",
        build_file = Label("//rules/rust/remote:BUILD.erased-serde-0.3.13.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fail__0_4_0",
        url = "https://crates.io/api/v1/crates/fail/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "fail-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.fail-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__failure__0_1_8",
        url = "https://crates.io/api/v1/crates/failure/0.1.8/download",
        type = "tar.gz",
        strip_prefix = "failure-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.failure-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__failure_derive__0_1_8",
        url = "https://crates.io/api/v1/crates/failure_derive/0.1.8/download",
        type = "tar.gz",
        strip_prefix = "failure_derive-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.failure_derive-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fallible_iterator__0_2_0",
        url = "https://crates.io/api/v1/crates/fallible-iterator/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "fallible-iterator-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.fallible-iterator-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fancy_regex__0_3_5",
        url = "https://crates.io/api/v1/crates/fancy-regex/0.3.5/download",
        type = "tar.gz",
        strip_prefix = "fancy-regex-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.fancy-regex-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__filetime__0_2_13",
        url = "https://crates.io/api/v1/crates/filetime/0.2.13/download",
        type = "tar.gz",
        strip_prefix = "filetime-0.2.13",
        build_file = Label("//rules/rust/remote:BUILD.filetime-0.2.13.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__flate2__1_0_19",
        url = "https://crates.io/api/v1/crates/flate2/1.0.19/download",
        type = "tar.gz",
        strip_prefix = "flate2-1.0.19",
        build_file = Label("//rules/rust/remote:BUILD.flate2-1.0.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fnv__1_0_7",
        url = "https://crates.io/api/v1/crates/fnv/1.0.7/download",
        type = "tar.gz",
        strip_prefix = "fnv-1.0.7",
        build_file = Label("//rules/rust/remote:BUILD.fnv-1.0.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__form_urlencoded__1_0_0",
        url = "https://crates.io/api/v1/crates/form_urlencoded/1.0.0/download",
        type = "tar.gz",
        strip_prefix = "form_urlencoded-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.form_urlencoded-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fs2__0_4_3",
        url = "https://crates.io/api/v1/crates/fs2/0.4.3/download",
        type = "tar.gz",
        strip_prefix = "fs2-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.fs2-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fst__0_3_5",
        url = "https://crates.io/api/v1/crates/fst/0.3.5/download",
        type = "tar.gz",
        strip_prefix = "fst-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.fst-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fst__0_4_5",
        url = "https://crates.io/api/v1/crates/fst/0.4.5/download",
        type = "tar.gz",
        strip_prefix = "fst-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.fst-0.4.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fuchsia_cprng__0_1_1",
        url = "https://crates.io/api/v1/crates/fuchsia-cprng/0.1.1/download",
        type = "tar.gz",
        strip_prefix = "fuchsia-cprng-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.fuchsia-cprng-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fuchsia_zircon__0_3_3",
        url = "https://crates.io/api/v1/crates/fuchsia-zircon/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "fuchsia-zircon-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.fuchsia-zircon-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fuchsia_zircon_sys__0_3_3",
        url = "https://crates.io/api/v1/crates/fuchsia-zircon-sys/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "fuchsia-zircon-sys-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.fuchsia-zircon-sys-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures__0_3_10",
        url = "https://crates.io/api/v1/crates/futures/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_channel__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-channel/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-channel-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-channel-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_core__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-core/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-core-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-core-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_executor__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-executor/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-executor-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-executor-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_io__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-io/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-io-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-io-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_macro__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-macro/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-macro-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-macro-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_sink__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-sink/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-sink-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-sink-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_task__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-task/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-task-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-task-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_util__0_3_10",
        url = "https://crates.io/api/v1/crates/futures-util/0.3.10/download",
        type = "tar.gz",
        strip_prefix = "futures-util-0.3.10",
        build_file = Label("//rules/rust/remote:BUILD.futures-util-0.3.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fxhash__0_2_1",
        url = "https://crates.io/api/v1/crates/fxhash/0.2.1/download",
        type = "tar.gz",
        strip_prefix = "fxhash-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.fxhash-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__generic_array__0_14_4",
        url = "https://crates.io/api/v1/crates/generic-array/0.14.4/download",
        type = "tar.gz",
        strip_prefix = "generic-array-0.14.4",
        build_file = Label("//rules/rust/remote:BUILD.generic-array-0.14.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__getrandom__0_1_16",
        url = "https://crates.io/api/v1/crates/getrandom/0.1.16/download",
        type = "tar.gz",
        strip_prefix = "getrandom-0.1.16",
        build_file = Label("//rules/rust/remote:BUILD.getrandom-0.1.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__getrandom__0_2_1",
        url = "https://crates.io/api/v1/crates/getrandom/0.2.1/download",
        type = "tar.gz",
        strip_prefix = "getrandom-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.getrandom-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__gimli__0_23_0",
        url = "https://crates.io/api/v1/crates/gimli/0.23.0/download",
        type = "tar.gz",
        strip_prefix = "gimli-0.23.0",
        build_file = Label("//rules/rust/remote:BUILD.gimli-0.23.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__grpc__0_8_2",
        url = "https://crates.io/api/v1/crates/grpc/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "grpc-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.grpc-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__grpc_compiler__0_8_2",
        url = "https://crates.io/api/v1/crates/grpc-compiler/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "grpc-compiler-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.grpc-compiler-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__h2__0_2_7",
        url = "https://crates.io/api/v1/crates/h2/0.2.7/download",
        type = "tar.gz",
        strip_prefix = "h2-0.2.7",
        build_file = Label("//rules/rust/remote:BUILD.h2-0.2.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__half__1_6_0",
        url = "https://crates.io/api/v1/crates/half/1.6.0/download",
        type = "tar.gz",
        strip_prefix = "half-1.6.0",
        build_file = Label("//rules/rust/remote:BUILD.half-1.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hashbrown__0_9_1",
        url = "https://crates.io/api/v1/crates/hashbrown/0.9.1/download",
        type = "tar.gz",
        strip_prefix = "hashbrown-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.hashbrown-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__heck__0_3_2",
        url = "https://crates.io/api/v1/crates/heck/0.3.2/download",
        type = "tar.gz",
        strip_prefix = "heck-0.3.2",
        build_file = Label("//rules/rust/remote:BUILD.heck-0.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hermit_abi__0_1_17",
        url = "https://crates.io/api/v1/crates/hermit-abi/0.1.17/download",
        type = "tar.gz",
        strip_prefix = "hermit-abi-0.1.17",
        build_file = Label("//rules/rust/remote:BUILD.hermit-abi-0.1.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hmac__0_10_1",
        url = "https://crates.io/api/v1/crates/hmac/0.10.1/download",
        type = "tar.gz",
        strip_prefix = "hmac-0.10.1",
        build_file = Label("//rules/rust/remote:BUILD.hmac-0.10.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hmac__0_9_0",
        url = "https://crates.io/api/v1/crates/hmac/0.9.0/download",
        type = "tar.gz",
        strip_prefix = "hmac-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.hmac-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hostname__0_3_1",
        url = "https://crates.io/api/v1/crates/hostname/0.3.1/download",
        type = "tar.gz",
        strip_prefix = "hostname-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.hostname-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__htmlescape__0_3_1",
        url = "https://crates.io/api/v1/crates/htmlescape/0.3.1/download",
        type = "tar.gz",
        strip_prefix = "htmlescape-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.htmlescape-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__http__0_2_3",
        url = "https://crates.io/api/v1/crates/http/0.2.3/download",
        type = "tar.gz",
        strip_prefix = "http-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.http-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__httparse__1_3_4",
        url = "https://crates.io/api/v1/crates/httparse/1.3.4/download",
        type = "tar.gz",
        strip_prefix = "httparse-1.3.4",
        build_file = Label("//rules/rust/remote:BUILD.httparse-1.3.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__httpbis__0_9_1",
        url = "https://crates.io/api/v1/crates/httpbis/0.9.1/download",
        type = "tar.gz",
        strip_prefix = "httpbis-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.httpbis-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__humantime__1_3_0",
        url = "https://crates.io/api/v1/crates/humantime/1.3.0/download",
        type = "tar.gz",
        strip_prefix = "humantime-1.3.0",
        build_file = Label("//rules/rust/remote:BUILD.humantime-1.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__humantime__2_1_0",
        url = "https://crates.io/api/v1/crates/humantime/2.1.0/download",
        type = "tar.gz",
        strip_prefix = "humantime-2.1.0",
        build_file = Label("//rules/rust/remote:BUILD.humantime-2.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__idna__0_2_0",
        url = "https://crates.io/api/v1/crates/idna/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "idna-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.idna-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__indexmap__1_6_1",
        url = "https://crates.io/api/v1/crates/indexmap/1.6.1/download",
        type = "tar.gz",
        strip_prefix = "indexmap-1.6.1",
        build_file = Label("//rules/rust/remote:BUILD.indexmap-1.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__instant__0_1_9",
        url = "https://crates.io/api/v1/crates/instant/0.1.9/download",
        type = "tar.gz",
        strip_prefix = "instant-0.1.9",
        build_file = Label("//rules/rust/remote:BUILD.instant-0.1.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__integer_encoding__2_1_2",
        url = "https://crates.io/api/v1/crates/integer-encoding/2.1.2/download",
        type = "tar.gz",
        strip_prefix = "integer-encoding-2.1.2",
        build_file = Label("//rules/rust/remote:BUILD.integer-encoding-2.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__iovec__0_1_4",
        url = "https://crates.io/api/v1/crates/iovec/0.1.4/download",
        type = "tar.gz",
        strip_prefix = "iovec-0.1.4",
        build_file = Label("//rules/rust/remote:BUILD.iovec-0.1.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ipconfig__0_2_2",
        url = "https://crates.io/api/v1/crates/ipconfig/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "ipconfig-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.ipconfig-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itertools__0_9_0",
        url = "https://crates.io/api/v1/crates/itertools/0.9.0/download",
        type = "tar.gz",
        strip_prefix = "itertools-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.itertools-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itoa__0_4_7",
        url = "https://crates.io/api/v1/crates/itoa/0.4.7/download",
        type = "tar.gz",
        strip_prefix = "itoa-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.itoa-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__js_sys__0_3_46",
        url = "https://crates.io/api/v1/crates/js-sys/0.3.46/download",
        type = "tar.gz",
        strip_prefix = "js-sys-0.3.46",
        build_file = Label("//rules/rust/remote:BUILD.js-sys-0.3.46.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__kernel32_sys__0_2_2",
        url = "https://crates.io/api/v1/crates/kernel32-sys/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "kernel32-sys-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.kernel32-sys-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__language_tags__0_2_2",
        url = "https://crates.io/api/v1/crates/language-tags/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "language-tags-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.language-tags-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lazy_static__1_4_0",
        url = "https://crates.io/api/v1/crates/lazy_static/1.4.0/download",
        type = "tar.gz",
        strip_prefix = "lazy_static-1.4.0",
        build_file = Label("//rules/rust/remote:BUILD.lazy_static-1.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__levenshtein_automata__0_1_1",
        url = "https://crates.io/api/v1/crates/levenshtein_automata/0.1.1/download",
        type = "tar.gz",
        strip_prefix = "levenshtein_automata-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.levenshtein_automata-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lexical_core__0_7_4",
        url = "https://crates.io/api/v1/crates/lexical-core/0.7.4/download",
        type = "tar.gz",
        strip_prefix = "lexical-core-0.7.4",
        build_file = Label("//rules/rust/remote:BUILD.lexical-core-0.7.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__libc__0_2_82",
        url = "https://crates.io/api/v1/crates/libc/0.2.82/download",
        type = "tar.gz",
        strip_prefix = "libc-0.2.82",
        build_file = Label("//rules/rust/remote:BUILD.libc-0.2.82.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__linked_hash_map__0_3_0",
        url = "https://crates.io/api/v1/crates/linked-hash-map/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "linked-hash-map-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.linked-hash-map-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__linked_hash_map__0_5_4",
        url = "https://crates.io/api/v1/crates/linked-hash-map/0.5.4/download",
        type = "tar.gz",
        strip_prefix = "linked-hash-map-0.5.4",
        build_file = Label("//rules/rust/remote:BUILD.linked-hash-map-0.5.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lock_api__0_4_2",
        url = "https://crates.io/api/v1/crates/lock_api/0.4.2/download",
        type = "tar.gz",
        strip_prefix = "lock_api-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.lock_api-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log__0_4_13",
        url = "https://crates.io/api/v1/crates/log/0.4.13/download",
        type = "tar.gz",
        strip_prefix = "log-0.4.13",
        build_file = Label("//rules/rust/remote:BUILD.log-0.4.13.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log_mdc__0_1_0",
        url = "https://crates.io/api/v1/crates/log-mdc/0.1.0/download",
        type = "tar.gz",
        strip_prefix = "log-mdc-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.log-mdc-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log_ndc__0_2_0",
        url = "https://crates.io/api/v1/crates/log-ndc/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "log-ndc-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.log-ndc-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log4rs__0_10_0",
        url = "https://crates.io/api/v1/crates/log4rs/0.10.0/download",
        type = "tar.gz",
        strip_prefix = "log4rs-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.log4rs-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lru__0_6_3",
        url = "https://crates.io/api/v1/crates/lru/0.6.3/download",
        type = "tar.gz",
        strip_prefix = "lru-0.6.3",
        build_file = Label("//rules/rust/remote:BUILD.lru-0.6.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lru_cache__0_1_2",
        url = "https://crates.io/api/v1/crates/lru-cache/0.1.2/download",
        type = "tar.gz",
        strip_prefix = "lru-cache-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.lru-cache-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lz4__1_23_2",
        url = "https://crates.io/api/v1/crates/lz4/1.23.2/download",
        type = "tar.gz",
        strip_prefix = "lz4-1.23.2",
        build_file = Label("//rules/rust/remote:BUILD.lz4-1.23.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lz4_sys__1_9_2",
        url = "https://crates.io/api/v1/crates/lz4-sys/1.9.2/download",
        type = "tar.gz",
        strip_prefix = "lz4-sys-1.9.2",
        build_file = Label("//rules/rust/remote:BUILD.lz4-sys-1.9.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__maplit__1_0_2",
        url = "https://crates.io/api/v1/crates/maplit/1.0.2/download",
        type = "tar.gz",
        strip_prefix = "maplit-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.maplit-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__match_cfg__0_1_0",
        url = "https://crates.io/api/v1/crates/match_cfg/0.1.0/download",
        type = "tar.gz",
        strip_prefix = "match_cfg-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.match_cfg-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__matches__0_1_8",
        url = "https://crates.io/api/v1/crates/matches/0.1.8/download",
        type = "tar.gz",
        strip_prefix = "matches-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.matches-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__maybe_uninit__2_0_0",
        url = "https://crates.io/api/v1/crates/maybe-uninit/2.0.0/download",
        type = "tar.gz",
        strip_prefix = "maybe-uninit-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.maybe-uninit-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__md5__0_7_0",
        url = "https://crates.io/api/v1/crates/md5/0.7.0/download",
        type = "tar.gz",
        strip_prefix = "md5-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.md5-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memchr__2_3_4",
        url = "https://crates.io/api/v1/crates/memchr/2.3.4/download",
        type = "tar.gz",
        strip_prefix = "memchr-2.3.4",
        build_file = Label("//rules/rust/remote:BUILD.memchr-2.3.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memmap__0_7_0",
        url = "https://crates.io/api/v1/crates/memmap/0.7.0/download",
        type = "tar.gz",
        strip_prefix = "memmap-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.memmap-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memoffset__0_5_6",
        url = "https://crates.io/api/v1/crates/memoffset/0.5.6/download",
        type = "tar.gz",
        strip_prefix = "memoffset-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.memoffset-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memoffset__0_6_1",
        url = "https://crates.io/api/v1/crates/memoffset/0.6.1/download",
        type = "tar.gz",
        strip_prefix = "memoffset-0.6.1",
        build_file = Label("//rules/rust/remote:BUILD.memoffset-0.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mime__0_3_16",
        url = "https://crates.io/api/v1/crates/mime/0.3.16/download",
        type = "tar.gz",
        strip_prefix = "mime-0.3.16",
        build_file = Label("//rules/rust/remote:BUILD.mime-0.3.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miniz_oxide__0_4_3",
        url = "https://crates.io/api/v1/crates/miniz_oxide/0.4.3/download",
        type = "tar.gz",
        strip_prefix = "miniz_oxide-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.miniz_oxide-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio__0_6_23",
        url = "https://crates.io/api/v1/crates/mio/0.6.23/download",
        type = "tar.gz",
        strip_prefix = "mio-0.6.23",
        build_file = Label("//rules/rust/remote:BUILD.mio-0.6.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio__0_7_7",
        url = "https://crates.io/api/v1/crates/mio/0.7.7/download",
        type = "tar.gz",
        strip_prefix = "mio-0.7.7",
        build_file = Label("//rules/rust/remote:BUILD.mio-0.7.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio_named_pipes__0_1_7",
        url = "https://crates.io/api/v1/crates/mio-named-pipes/0.1.7/download",
        type = "tar.gz",
        strip_prefix = "mio-named-pipes-0.1.7",
        build_file = Label("//rules/rust/remote:BUILD.mio-named-pipes-0.1.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio_uds__0_6_8",
        url = "https://crates.io/api/v1/crates/mio-uds/0.6.8/download",
        type = "tar.gz",
        strip_prefix = "mio-uds-0.6.8",
        build_file = Label("//rules/rust/remote:BUILD.mio-uds-0.6.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miow__0_2_2",
        url = "https://crates.io/api/v1/crates/miow/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "miow-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.miow-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miow__0_3_6",
        url = "https://crates.io/api/v1/crates/miow/0.3.6/download",
        type = "tar.gz",
        strip_prefix = "miow-0.3.6",
        build_file = Label("//rules/rust/remote:BUILD.miow-0.3.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__murmurhash32__0_2_0",
        url = "https://crates.io/api/v1/crates/murmurhash32/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "murmurhash32-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.murmurhash32-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__net2__0_2_37",
        url = "https://crates.io/api/v1/crates/net2/0.2.37/download",
        type = "tar.gz",
        strip_prefix = "net2-0.2.37",
        build_file = Label("//rules/rust/remote:BUILD.net2-0.2.37.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__nix__0_14_1",
        url = "https://crates.io/api/v1/crates/nix/0.14.1/download",
        type = "tar.gz",
        strip_prefix = "nix-0.14.1",
        build_file = Label("//rules/rust/remote:BUILD.nix-0.14.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__nom__5_1_2",
        url = "https://crates.io/api/v1/crates/nom/5.1.2/download",
        type = "tar.gz",
        strip_prefix = "nom-5.1.2",
        build_file = Label("//rules/rust/remote:BUILD.nom-5.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ntapi__0_3_6",
        url = "https://crates.io/api/v1/crates/ntapi/0.3.6/download",
        type = "tar.gz",
        strip_prefix = "ntapi-0.3.6",
        build_file = Label("//rules/rust/remote:BUILD.ntapi-0.3.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_bigint__0_3_1",
        url = "https://crates.io/api/v1/crates/num-bigint/0.3.1/download",
        type = "tar.gz",
        strip_prefix = "num-bigint-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.num-bigint-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_integer__0_1_44",
        url = "https://crates.io/api/v1/crates/num-integer/0.1.44/download",
        type = "tar.gz",
        strip_prefix = "num-integer-0.1.44",
        build_file = Label("//rules/rust/remote:BUILD.num-integer-0.1.44.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_traits__0_1_43",
        url = "https://crates.io/api/v1/crates/num-traits/0.1.43/download",
        type = "tar.gz",
        strip_prefix = "num-traits-0.1.43",
        build_file = Label("//rules/rust/remote:BUILD.num-traits-0.1.43.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_traits__0_2_14",
        url = "https://crates.io/api/v1/crates/num-traits/0.2.14/download",
        type = "tar.gz",
        strip_prefix = "num-traits-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.num-traits-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_cpus__1_13_0",
        url = "https://crates.io/api/v1/crates/num_cpus/1.13.0/download",
        type = "tar.gz",
        strip_prefix = "num_cpus-1.13.0",
        build_file = Label("//rules/rust/remote:BUILD.num_cpus-1.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__object__0_22_0",
        url = "https://crates.io/api/v1/crates/object/0.22.0/download",
        type = "tar.gz",
        strip_prefix = "object-0.22.0",
        build_file = Label("//rules/rust/remote:BUILD.object-0.22.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__once_cell__1_5_2",
        url = "https://crates.io/api/v1/crates/once_cell/1.5.2/download",
        type = "tar.gz",
        strip_prefix = "once_cell-1.5.2",
        build_file = Label("//rules/rust/remote:BUILD.once_cell-1.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__oorandom__11_1_3",
        url = "https://crates.io/api/v1/crates/oorandom/11.1.3/download",
        type = "tar.gz",
        strip_prefix = "oorandom-11.1.3",
        build_file = Label("//rules/rust/remote:BUILD.oorandom-11.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__opaque_debug__0_3_0",
        url = "https://crates.io/api/v1/crates/opaque-debug/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "opaque-debug-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.opaque-debug-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ordered_float__1_1_1",
        url = "https://crates.io/api/v1/crates/ordered-float/1.1.1/download",
        type = "tar.gz",
        strip_prefix = "ordered-float-1.1.1",
        build_file = Label("//rules/rust/remote:BUILD.ordered-float-1.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__owned_read__0_4_1",
        url = "https://crates.io/api/v1/crates/owned-read/0.4.1/download",
        type = "tar.gz",
        strip_prefix = "owned-read-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.owned-read-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__owning_ref__0_4_1",
        url = "https://crates.io/api/v1/crates/owning_ref/0.4.1/download",
        type = "tar.gz",
        strip_prefix = "owning_ref-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.owning_ref-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot__0_11_1",
        url = "https://crates.io/api/v1/crates/parking_lot/0.11.1/download",
        type = "tar.gz",
        strip_prefix = "parking_lot-0.11.1",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot-0.11.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot_core__0_8_2",
        url = "https://crates.io/api/v1/crates/parking_lot_core/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "parking_lot_core-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot_core-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__percent_encoding__2_1_0",
        url = "https://crates.io/api/v1/crates/percent-encoding/2.1.0/download",
        type = "tar.gz",
        strip_prefix = "percent-encoding-2.1.0",
        build_file = Label("//rules/rust/remote:BUILD.percent-encoding-2.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__phf__0_8_0",
        url = "https://crates.io/api/v1/crates/phf/0.8.0/download",
        type = "tar.gz",
        strip_prefix = "phf-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.phf-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__phf_shared__0_8_0",
        url = "https://crates.io/api/v1/crates/phf_shared/0.8.0/download",
        type = "tar.gz",
        strip_prefix = "phf_shared-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.phf_shared-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project__0_4_27",
        url = "https://crates.io/api/v1/crates/pin-project/0.4.27/download",
        type = "tar.gz",
        strip_prefix = "pin-project-0.4.27",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-0.4.27.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project__1_0_4",
        url = "https://crates.io/api/v1/crates/pin-project/1.0.4/download",
        type = "tar.gz",
        strip_prefix = "pin-project-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_internal__0_4_27",
        url = "https://crates.io/api/v1/crates/pin-project-internal/0.4.27/download",
        type = "tar.gz",
        strip_prefix = "pin-project-internal-0.4.27",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-internal-0.4.27.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_internal__1_0_4",
        url = "https://crates.io/api/v1/crates/pin-project-internal/1.0.4/download",
        type = "tar.gz",
        strip_prefix = "pin-project-internal-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-internal-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_lite__0_1_11",
        url = "https://crates.io/api/v1/crates/pin-project-lite/0.1.11/download",
        type = "tar.gz",
        strip_prefix = "pin-project-lite-0.1.11",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-lite-0.1.11.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_lite__0_2_4",
        url = "https://crates.io/api/v1/crates/pin-project-lite/0.2.4/download",
        type = "tar.gz",
        strip_prefix = "pin-project-lite-0.2.4",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-lite-0.2.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_utils__0_1_0",
        url = "https://crates.io/api/v1/crates/pin-utils/0.1.0/download",
        type = "tar.gz",
        strip_prefix = "pin-utils-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.pin-utils-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__plotters__0_2_15",
        url = "https://crates.io/api/v1/crates/plotters/0.2.15/download",
        type = "tar.gz",
        strip_prefix = "plotters-0.2.15",
        build_file = Label("//rules/rust/remote:BUILD.plotters-0.2.15.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres__0_17_5",
        url = "https://crates.io/api/v1/crates/postgres/0.17.5/download",
        type = "tar.gz",
        strip_prefix = "postgres-0.17.5",
        build_file = Label("//rules/rust/remote:BUILD.postgres-0.17.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_derive__0_4_0",
        url = "https://crates.io/api/v1/crates/postgres-derive/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "postgres-derive-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.postgres-derive-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_protocol__0_5_3",
        url = "https://crates.io/api/v1/crates/postgres-protocol/0.5.3/download",
        type = "tar.gz",
        strip_prefix = "postgres-protocol-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.postgres-protocol-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_protocol__0_6_0",
        url = "https://crates.io/api/v1/crates/postgres-protocol/0.6.0/download",
        type = "tar.gz",
        strip_prefix = "postgres-protocol-0.6.0",
        build_file = Label("//rules/rust/remote:BUILD.postgres-protocol-0.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_types__0_1_3",
        url = "https://crates.io/api/v1/crates/postgres-types/0.1.3/download",
        type = "tar.gz",
        strip_prefix = "postgres-types-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.postgres-types-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_types__0_2_0",
        url = "https://crates.io/api/v1/crates/postgres-types/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "postgres-types-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.postgres-types-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ppv_lite86__0_2_10",
        url = "https://crates.io/api/v1/crates/ppv-lite86/0.2.10/download",
        type = "tar.gz",
        strip_prefix = "ppv-lite86-0.2.10",
        build_file = Label("//rules/rust/remote:BUILD.ppv-lite86-0.2.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro_hack__0_5_19",
        url = "https://crates.io/api/v1/crates/proc-macro-hack/0.5.19/download",
        type = "tar.gz",
        strip_prefix = "proc-macro-hack-0.5.19",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro-hack-0.5.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro_nested__0_1_7",
        url = "https://crates.io/api/v1/crates/proc-macro-nested/0.1.7/download",
        type = "tar.gz",
        strip_prefix = "proc-macro-nested-0.1.7",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro-nested-0.1.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro2__1_0_24",
        url = "https://crates.io/api/v1/crates/proc-macro2/1.0.24/download",
        type = "tar.gz",
        strip_prefix = "proc-macro2-1.0.24",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro2-1.0.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proptest__0_10_1",
        url = "https://crates.io/api/v1/crates/proptest/0.10.1/download",
        type = "tar.gz",
        strip_prefix = "proptest-0.10.1",
        build_file = Label("//rules/rust/remote:BUILD.proptest-0.10.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__protobuf__2_20_0",
        url = "https://crates.io/api/v1/crates/protobuf/2.20.0/download",
        type = "tar.gz",
        strip_prefix = "protobuf-2.20.0",
        build_file = Label("//rules/rust/remote:BUILD.protobuf-2.20.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__protobuf_codegen__2_20_0",
        url = "https://crates.io/api/v1/crates/protobuf-codegen/2.20.0/download",
        type = "tar.gz",
        strip_prefix = "protobuf-codegen-2.20.0",
        build_file = Label("//rules/rust/remote:BUILD.protobuf-codegen-2.20.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__quick_error__1_2_3",
        url = "https://crates.io/api/v1/crates/quick-error/1.2.3/download",
        type = "tar.gz",
        strip_prefix = "quick-error-1.2.3",
        build_file = Label("//rules/rust/remote:BUILD.quick-error-1.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__quote__1_0_8",
        url = "https://crates.io/api/v1/crates/quote/1.0.8/download",
        type = "tar.gz",
        strip_prefix = "quote-1.0.8",
        build_file = Label("//rules/rust/remote:BUILD.quote-1.0.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__r2d2__0_8_9",
        url = "https://crates.io/api/v1/crates/r2d2/0.8.9/download",
        type = "tar.gz",
        strip_prefix = "r2d2-0.8.9",
        build_file = Label("//rules/rust/remote:BUILD.r2d2-0.8.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__r2d2_postgres__0_16_0",
        url = "https://crates.io/api/v1/crates/r2d2_postgres/0.16.0/download",
        type = "tar.gz",
        strip_prefix = "r2d2_postgres-0.16.0",
        build_file = Label("//rules/rust/remote:BUILD.r2d2_postgres-0.16.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_4_6",
        url = "https://crates.io/api/v1/crates/rand/0.4.6/download",
        type = "tar.gz",
        strip_prefix = "rand-0.4.6",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.4.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_5_6",
        url = "https://crates.io/api/v1/crates/rand/0.5.6/download",
        type = "tar.gz",
        strip_prefix = "rand-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_7_3",
        url = "https://crates.io/api/v1/crates/rand/0.7.3/download",
        type = "tar.gz",
        strip_prefix = "rand-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_8_2",
        url = "https://crates.io/api/v1/crates/rand/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "rand-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_chacha__0_2_2",
        url = "https://crates.io/api/v1/crates/rand_chacha/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "rand_chacha-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.rand_chacha-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_chacha__0_3_0",
        url = "https://crates.io/api/v1/crates/rand_chacha/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "rand_chacha-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_chacha-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_3_1",
        url = "https://crates.io/api/v1/crates/rand_core/0.3.1/download",
        type = "tar.gz",
        strip_prefix = "rand_core-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_4_2",
        url = "https://crates.io/api/v1/crates/rand_core/0.4.2/download",
        type = "tar.gz",
        strip_prefix = "rand_core-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_5_1",
        url = "https://crates.io/api/v1/crates/rand_core/0.5.1/download",
        type = "tar.gz",
        strip_prefix = "rand_core-0.5.1",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.5.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_6_1",
        url = "https://crates.io/api/v1/crates/rand_core/0.6.1/download",
        type = "tar.gz",
        strip_prefix = "rand_core-0.6.1",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_hc__0_2_0",
        url = "https://crates.io/api/v1/crates/rand_hc/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "rand_hc-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_hc-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_hc__0_3_0",
        url = "https://crates.io/api/v1/crates/rand_hc/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "rand_hc-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_hc-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_xorshift__0_2_0",
        url = "https://crates.io/api/v1/crates/rand_xorshift/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "rand_xorshift-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_xorshift-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rayon__1_5_0",
        url = "https://crates.io/api/v1/crates/rayon/1.5.0/download",
        type = "tar.gz",
        strip_prefix = "rayon-1.5.0",
        build_file = Label("//rules/rust/remote:BUILD.rayon-1.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rayon_core__1_9_0",
        url = "https://crates.io/api/v1/crates/rayon-core/1.9.0/download",
        type = "tar.gz",
        strip_prefix = "rayon-core-1.9.0",
        build_file = Label("//rules/rust/remote:BUILD.rayon-core-1.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rdrand__0_4_0",
        url = "https://crates.io/api/v1/crates/rdrand/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "rdrand-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.rdrand-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_syscall__0_1_57",
        url = "https://crates.io/api/v1/crates/redox_syscall/0.1.57/download",
        type = "tar.gz",
        strip_prefix = "redox_syscall-0.1.57",
        build_file = Label("//rules/rust/remote:BUILD.redox_syscall-0.1.57.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_syscall__0_2_4",
        url = "https://crates.io/api/v1/crates/redox_syscall/0.2.4/download",
        type = "tar.gz",
        strip_prefix = "redox_syscall-0.2.4",
        build_file = Label("//rules/rust/remote:BUILD.redox_syscall-0.2.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_users__0_3_5",
        url = "https://crates.io/api/v1/crates/redox_users/0.3.5/download",
        type = "tar.gz",
        strip_prefix = "redox_users-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.redox_users-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex__1_4_3",
        url = "https://crates.io/api/v1/crates/regex/1.4.3/download",
        type = "tar.gz",
        strip_prefix = "regex-1.4.3",
        build_file = Label("//rules/rust/remote:BUILD.regex-1.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_automata__0_1_9",
        url = "https://crates.io/api/v1/crates/regex-automata/0.1.9/download",
        type = "tar.gz",
        strip_prefix = "regex-automata-0.1.9",
        build_file = Label("//rules/rust/remote:BUILD.regex-automata-0.1.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_syntax__0_4_2",
        url = "https://crates.io/api/v1/crates/regex-syntax/0.4.2/download",
        type = "tar.gz",
        strip_prefix = "regex-syntax-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.regex-syntax-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_syntax__0_6_22",
        url = "https://crates.io/api/v1/crates/regex-syntax/0.6.22/download",
        type = "tar.gz",
        strip_prefix = "regex-syntax-0.6.22",
        build_file = Label("//rules/rust/remote:BUILD.regex-syntax-0.6.22.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__remove_dir_all__0_5_3",
        url = "https://crates.io/api/v1/crates/remove_dir_all/0.5.3/download",
        type = "tar.gz",
        strip_prefix = "remove_dir_all-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.remove_dir_all-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__reopen__1_0_2",
        url = "https://crates.io/api/v1/crates/reopen/1.0.2/download",
        type = "tar.gz",
        strip_prefix = "reopen-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.reopen-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__resolv_conf__0_7_0",
        url = "https://crates.io/api/v1/crates/resolv-conf/0.7.0/download",
        type = "tar.gz",
        strip_prefix = "resolv-conf-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.resolv-conf-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_argon2__0_8_3",
        url = "https://crates.io/api/v1/crates/rust-argon2/0.8.3/download",
        type = "tar.gz",
        strip_prefix = "rust-argon2-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.rust-argon2-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_ini__0_13_0",
        url = "https://crates.io/api/v1/crates/rust-ini/0.13.0/download",
        type = "tar.gz",
        strip_prefix = "rust-ini-0.13.0",
        build_file = Label("//rules/rust/remote:BUILD.rust-ini-0.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_stemmers__1_2_0",
        url = "https://crates.io/api/v1/crates/rust-stemmers/1.2.0/download",
        type = "tar.gz",
        strip_prefix = "rust-stemmers-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rust-stemmers-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustc_demangle__0_1_18",
        url = "https://crates.io/api/v1/crates/rustc-demangle/0.1.18/download",
        type = "tar.gz",
        strip_prefix = "rustc-demangle-0.1.18",
        build_file = Label("//rules/rust/remote:BUILD.rustc-demangle-0.1.18.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustc_serialize__0_3_24",
        url = "https://crates.io/api/v1/crates/rustc-serialize/0.3.24/download",
        type = "tar.gz",
        strip_prefix = "rustc-serialize-0.3.24",
        build_file = Label("//rules/rust/remote:BUILD.rustc-serialize-0.3.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustc_version__0_2_3",
        url = "https://crates.io/api/v1/crates/rustc_version/0.2.3/download",
        type = "tar.gz",
        strip_prefix = "rustc_version-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.rustc_version-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rusty_fork__0_3_0",
        url = "https://crates.io/api/v1/crates/rusty-fork/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "rusty-fork-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.rusty-fork-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ryu__1_0_5",
        url = "https://crates.io/api/v1/crates/ryu/1.0.5/download",
        type = "tar.gz",
        strip_prefix = "ryu-1.0.5",
        build_file = Label("//rules/rust/remote:BUILD.ryu-1.0.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__safemem__0_3_3",
        url = "https://crates.io/api/v1/crates/safemem/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "safemem-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.safemem-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__same_file__1_0_6",
        url = "https://crates.io/api/v1/crates/same-file/1.0.6/download",
        type = "tar.gz",
        strip_prefix = "same-file-1.0.6",
        build_file = Label("//rules/rust/remote:BUILD.same-file-1.0.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__scheduled_thread_pool__0_2_5",
        url = "https://crates.io/api/v1/crates/scheduled-thread-pool/0.2.5/download",
        type = "tar.gz",
        strip_prefix = "scheduled-thread-pool-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.scheduled-thread-pool-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__scopeguard__1_1_0",
        url = "https://crates.io/api/v1/crates/scopeguard/1.1.0/download",
        type = "tar.gz",
        strip_prefix = "scopeguard-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.scopeguard-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__semver__0_9_0",
        url = "https://crates.io/api/v1/crates/semver/0.9.0/download",
        type = "tar.gz",
        strip_prefix = "semver-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.semver-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__semver_parser__0_7_0",
        url = "https://crates.io/api/v1/crates/semver-parser/0.7.0/download",
        type = "tar.gz",
        strip_prefix = "semver-parser-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.semver-parser-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde__0_8_23",
        url = "https://crates.io/api/v1/crates/serde/0.8.23/download",
        type = "tar.gz",
        strip_prefix = "serde-0.8.23",
        build_file = Label("//rules/rust/remote:BUILD.serde-0.8.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde__1_0_119",
        url = "https://crates.io/api/v1/crates/serde/1.0.119/download",
        type = "tar.gz",
        strip_prefix = "serde-1.0.119",
        build_file = Label("//rules/rust/remote:BUILD.serde-1.0.119.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_hjson__0_9_1",
        url = "https://crates.io/api/v1/crates/serde-hjson/0.9.1/download",
        type = "tar.gz",
        strip_prefix = "serde-hjson-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.serde-hjson-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_value__0_6_0",
        url = "https://crates.io/api/v1/crates/serde-value/0.6.0/download",
        type = "tar.gz",
        strip_prefix = "serde-value-0.6.0",
        build_file = Label("//rules/rust/remote:BUILD.serde-value-0.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_cbor__0_11_1",
        url = "https://crates.io/api/v1/crates/serde_cbor/0.11.1/download",
        type = "tar.gz",
        strip_prefix = "serde_cbor-0.11.1",
        build_file = Label("//rules/rust/remote:BUILD.serde_cbor-0.11.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_derive__1_0_119",
        url = "https://crates.io/api/v1/crates/serde_derive/1.0.119/download",
        type = "tar.gz",
        strip_prefix = "serde_derive-1.0.119",
        build_file = Label("//rules/rust/remote:BUILD.serde_derive-1.0.119.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_json__1_0_61",
        url = "https://crates.io/api/v1/crates/serde_json/1.0.61/download",
        type = "tar.gz",
        strip_prefix = "serde_json-1.0.61",
        build_file = Label("//rules/rust/remote:BUILD.serde_json-1.0.61.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_qs__0_8_2",
        url = "https://crates.io/api/v1/crates/serde_qs/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "serde_qs-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.serde_qs-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_test__0_8_23",
        url = "https://crates.io/api/v1/crates/serde_test/0.8.23/download",
        type = "tar.gz",
        strip_prefix = "serde_test-0.8.23",
        build_file = Label("//rules/rust/remote:BUILD.serde_test-0.8.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_urlencoded__0_7_0",
        url = "https://crates.io/api/v1/crates/serde_urlencoded/0.7.0/download",
        type = "tar.gz",
        strip_prefix = "serde_urlencoded-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.serde_urlencoded-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_yaml__0_8_15",
        url = "https://crates.io/api/v1/crates/serde_yaml/0.8.15/download",
        type = "tar.gz",
        strip_prefix = "serde_yaml-0.8.15",
        build_file = Label("//rules/rust/remote:BUILD.serde_yaml-0.8.15.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha_1__0_9_2",
        url = "https://crates.io/api/v1/crates/sha-1/0.9.2/download",
        type = "tar.gz",
        strip_prefix = "sha-1-0.9.2",
        build_file = Label("//rules/rust/remote:BUILD.sha-1-0.9.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha1__0_6_0",
        url = "https://crates.io/api/v1/crates/sha1/0.6.0/download",
        type = "tar.gz",
        strip_prefix = "sha1-0.6.0",
        build_file = Label("//rules/rust/remote:BUILD.sha1-0.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha2__0_9_2",
        url = "https://crates.io/api/v1/crates/sha2/0.9.2/download",
        type = "tar.gz",
        strip_prefix = "sha2-0.9.2",
        build_file = Label("//rules/rust/remote:BUILD.sha2-0.9.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook__0_2_3",
        url = "https://crates.io/api/v1/crates/signal-hook/0.2.3/download",
        type = "tar.gz",
        strip_prefix = "signal-hook-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook__0_3_3",
        url = "https://crates.io/api/v1/crates/signal-hook/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "signal-hook-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook_registry__1_3_0",
        url = "https://crates.io/api/v1/crates/signal-hook-registry/1.3.0/download",
        type = "tar.gz",
        strip_prefix = "signal-hook-registry-1.3.0",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-registry-1.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__siphasher__0_3_3",
        url = "https://crates.io/api/v1/crates/siphasher/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "siphasher-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.siphasher-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slab__0_4_2",
        url = "https://crates.io/api/v1/crates/slab/0.4.2/download",
        type = "tar.gz",
        strip_prefix = "slab-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.slab-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog__2_7_0",
        url = "https://crates.io/api/v1/crates/slog/2.7.0/download",
        type = "tar.gz",
        strip_prefix = "slog-2.7.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-2.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_async__2_6_0",
        url = "https://crates.io/api/v1/crates/slog-async/2.6.0/download",
        type = "tar.gz",
        strip_prefix = "slog-async-2.6.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-async-2.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_json__2_3_0",
        url = "https://crates.io/api/v1/crates/slog-json/2.3.0/download",
        type = "tar.gz",
        strip_prefix = "slog-json-2.3.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-json-2.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_scope__4_4_0",
        url = "https://crates.io/api/v1/crates/slog-scope/4.4.0/download",
        type = "tar.gz",
        strip_prefix = "slog-scope-4.4.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-scope-4.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_stdlog__4_1_0",
        url = "https://crates.io/api/v1/crates/slog-stdlog/4.1.0/download",
        type = "tar.gz",
        strip_prefix = "slog-stdlog-4.1.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-stdlog-4.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_term__2_6_0",
        url = "https://crates.io/api/v1/crates/slog-term/2.6.0/download",
        type = "tar.gz",
        strip_prefix = "slog-term-2.6.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-term-2.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_derive__0_2_0",
        url = "https://crates.io/api/v1/crates/slog_derive/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "slog_derive-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.slog_derive-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__smallvec__1_6_1",
        url = "https://crates.io/api/v1/crates/smallvec/1.6.1/download",
        type = "tar.gz",
        strip_prefix = "smallvec-1.6.1",
        build_file = Label("//rules/rust/remote:BUILD.smallvec-1.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__smawk__0_3_0",
        url = "https://crates.io/api/v1/crates/smawk/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "smawk-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.smawk-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__snap__1_0_3",
        url = "https://crates.io/api/v1/crates/snap/1.0.3/download",
        type = "tar.gz",
        strip_prefix = "snap-1.0.3",
        build_file = Label("//rules/rust/remote:BUILD.snap-1.0.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__socket2__0_3_19",
        url = "https://crates.io/api/v1/crates/socket2/0.3.19/download",
        type = "tar.gz",
        strip_prefix = "socket2-0.3.19",
        build_file = Label("//rules/rust/remote:BUILD.socket2-0.3.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stable_deref_trait__1_2_0",
        url = "https://crates.io/api/v1/crates/stable_deref_trait/1.2.0/download",
        type = "tar.gz",
        strip_prefix = "stable_deref_trait-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.stable_deref_trait-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__standback__0_2_14",
        url = "https://crates.io/api/v1/crates/standback/0.2.14/download",
        type = "tar.gz",
        strip_prefix = "standback-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.standback-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__static_assertions__1_1_0",
        url = "https://crates.io/api/v1/crates/static_assertions/1.1.0/download",
        type = "tar.gz",
        strip_prefix = "static_assertions-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.static_assertions-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb__0_4_20",
        url = "https://crates.io/api/v1/crates/stdweb/0.4.20/download",
        type = "tar.gz",
        strip_prefix = "stdweb-0.4.20",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-0.4.20.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb_derive__0_5_3",
        url = "https://crates.io/api/v1/crates/stdweb-derive/0.5.3/download",
        type = "tar.gz",
        strip_prefix = "stdweb-derive-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-derive-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb_internal_macros__0_2_9",
        url = "https://crates.io/api/v1/crates/stdweb-internal-macros/0.2.9/download",
        type = "tar.gz",
        strip_prefix = "stdweb-internal-macros-0.2.9",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-internal-macros-0.2.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb_internal_runtime__0_1_5",
        url = "https://crates.io/api/v1/crates/stdweb-internal-runtime/0.1.5/download",
        type = "tar.gz",
        strip_prefix = "stdweb-internal-runtime-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-internal-runtime-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stringprep__0_1_2",
        url = "https://crates.io/api/v1/crates/stringprep/0.1.2/download",
        type = "tar.gz",
        strip_prefix = "stringprep-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.stringprep-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strsim__0_8_0",
        url = "https://crates.io/api/v1/crates/strsim/0.8.0/download",
        type = "tar.gz",
        strip_prefix = "strsim-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.strsim-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strum__0_20_0",
        url = "https://crates.io/api/v1/crates/strum/0.20.0/download",
        type = "tar.gz",
        strip_prefix = "strum-0.20.0",
        build_file = Label("//rules/rust/remote:BUILD.strum-0.20.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strum_macros__0_20_1",
        url = "https://crates.io/api/v1/crates/strum_macros/0.20.1/download",
        type = "tar.gz",
        strip_prefix = "strum_macros-0.20.1",
        build_file = Label("//rules/rust/remote:BUILD.strum_macros-0.20.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__subtle__2_4_0",
        url = "https://crates.io/api/v1/crates/subtle/2.4.0/download",
        type = "tar.gz",
        strip_prefix = "subtle-2.4.0",
        build_file = Label("//rules/rust/remote:BUILD.subtle-2.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__syn__1_0_58",
        url = "https://crates.io/api/v1/crates/syn/1.0.58/download",
        type = "tar.gz",
        strip_prefix = "syn-1.0.58",
        build_file = Label("//rules/rust/remote:BUILD.syn-1.0.58.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__synstructure__0_12_4",
        url = "https://crates.io/api/v1/crates/synstructure/0.12.4/download",
        type = "tar.gz",
        strip_prefix = "synstructure-0.12.4",
        build_file = Label("//rules/rust/remote:BUILD.synstructure-0.12.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__take_mut__0_2_2",
        url = "https://crates.io/api/v1/crates/take_mut/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "take_mut-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.take_mut-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_fst__0_3_0",
        url = "https://crates.io/api/v1/crates/tantivy-fst/0.3.0/download",
        type = "tar.gz",
        strip_prefix = "tantivy-fst-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-fst-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tar__0_4_30",
        url = "https://crates.io/api/v1/crates/tar/0.4.30/download",
        type = "tar.gz",
        strip_prefix = "tar-0.4.30",
        build_file = Label("//rules/rust/remote:BUILD.tar-0.4.30.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tempdir__0_3_7",
        url = "https://crates.io/api/v1/crates/tempdir/0.3.7/download",
        type = "tar.gz",
        strip_prefix = "tempdir-0.3.7",
        build_file = Label("//rules/rust/remote:BUILD.tempdir-0.3.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tempfile__3_2_0",
        url = "https://crates.io/api/v1/crates/tempfile/3.2.0/download",
        type = "tar.gz",
        strip_prefix = "tempfile-3.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tempfile-3.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__term__0_6_1",
        url = "https://crates.io/api/v1/crates/term/0.6.1/download",
        type = "tar.gz",
        strip_prefix = "term-0.6.1",
        build_file = Label("//rules/rust/remote:BUILD.term-0.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__termcolor__1_1_2",
        url = "https://crates.io/api/v1/crates/termcolor/1.1.2/download",
        type = "tar.gz",
        strip_prefix = "termcolor-1.1.2",
        build_file = Label("//rules/rust/remote:BUILD.termcolor-1.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__textwrap__0_11_0",
        url = "https://crates.io/api/v1/crates/textwrap/0.11.0/download",
        type = "tar.gz",
        strip_prefix = "textwrap-0.11.0",
        build_file = Label("//rules/rust/remote:BUILD.textwrap-0.11.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__textwrap__0_13_2",
        url = "https://crates.io/api/v1/crates/textwrap/0.13.2/download",
        type = "tar.gz",
        strip_prefix = "textwrap-0.13.2",
        build_file = Label("//rules/rust/remote:BUILD.textwrap-0.13.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thiserror__1_0_23",
        url = "https://crates.io/api/v1/crates/thiserror/1.0.23/download",
        type = "tar.gz",
        strip_prefix = "thiserror-1.0.23",
        build_file = Label("//rules/rust/remote:BUILD.thiserror-1.0.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thiserror_impl__1_0_23",
        url = "https://crates.io/api/v1/crates/thiserror-impl/1.0.23/download",
        type = "tar.gz",
        strip_prefix = "thiserror-impl-1.0.23",
        build_file = Label("//rules/rust/remote:BUILD.thiserror-impl-1.0.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thread_id__3_3_0",
        url = "https://crates.io/api/v1/crates/thread-id/3.3.0/download",
        type = "tar.gz",
        strip_prefix = "thread-id-3.3.0",
        build_file = Label("//rules/rust/remote:BUILD.thread-id-3.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thread_local__1_1_0",
        url = "https://crates.io/api/v1/crates/thread_local/1.1.0/download",
        type = "tar.gz",
        strip_prefix = "thread_local-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.thread_local-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__threadpool__1_8_1",
        url = "https://crates.io/api/v1/crates/threadpool/1.8.1/download",
        type = "tar.gz",
        strip_prefix = "threadpool-1.8.1",
        build_file = Label("//rules/rust/remote:BUILD.threadpool-1.8.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time__0_1_43",
        url = "https://crates.io/api/v1/crates/time/0.1.43/download",
        type = "tar.gz",
        strip_prefix = "time-0.1.43",
        build_file = Label("//rules/rust/remote:BUILD.time-0.1.43.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time__0_2_24",
        url = "https://crates.io/api/v1/crates/time/0.2.24/download",
        type = "tar.gz",
        strip_prefix = "time-0.2.24",
        build_file = Label("//rules/rust/remote:BUILD.time-0.2.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time_macros__0_1_1",
        url = "https://crates.io/api/v1/crates/time-macros/0.1.1/download",
        type = "tar.gz",
        strip_prefix = "time-macros-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.time-macros-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time_macros_impl__0_1_1",
        url = "https://crates.io/api/v1/crates/time-macros-impl/0.1.1/download",
        type = "tar.gz",
        strip_prefix = "time-macros-impl-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.time-macros-impl-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tinytemplate__1_2_0",
        url = "https://crates.io/api/v1/crates/tinytemplate/1.2.0/download",
        type = "tar.gz",
        strip_prefix = "tinytemplate-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tinytemplate-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tinyvec__1_1_0",
        url = "https://crates.io/api/v1/crates/tinyvec/1.1.0/download",
        type = "tar.gz",
        strip_prefix = "tinyvec-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.tinyvec-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tinyvec_macros__0_1_0",
        url = "https://crates.io/api/v1/crates/tinyvec_macros/0.1.0/download",
        type = "tar.gz",
        strip_prefix = "tinyvec_macros-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.tinyvec_macros-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tls_api__0_4_0",
        url = "https://crates.io/api/v1/crates/tls-api/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "tls-api-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.tls-api-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tls_api_stub__0_4_0",
        url = "https://crates.io/api/v1/crates/tls-api-stub/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "tls-api-stub-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.tls-api-stub-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio__0_2_24",
        url = "https://crates.io/api/v1/crates/tokio/0.2.24/download",
        type = "tar.gz",
        strip_prefix = "tokio-0.2.24",
        build_file = Label("//rules/rust/remote:BUILD.tokio-0.2.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio__1_0_1",
        url = "https://crates.io/api/v1/crates/tokio/1.0.1/download",
        type = "tar.gz",
        strip_prefix = "tokio-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.tokio-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_macros__0_2_6",
        url = "https://crates.io/api/v1/crates/tokio-macros/0.2.6/download",
        type = "tar.gz",
        strip_prefix = "tokio-macros-0.2.6",
        build_file = Label("//rules/rust/remote:BUILD.tokio-macros-0.2.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_pg_mapper__0_2_0",
        url = "https://crates.io/api/v1/crates/tokio-pg-mapper/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "tokio-pg-mapper-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-pg-mapper-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_pg_mapper_derive__0_2_0",
        url = "https://crates.io/api/v1/crates/tokio-pg-mapper-derive/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "tokio-pg-mapper-derive-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-pg-mapper-derive-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_postgres__0_5_5",
        url = "https://crates.io/api/v1/crates/tokio-postgres/0.5.5/download",
        type = "tar.gz",
        strip_prefix = "tokio-postgres-0.5.5",
        build_file = Label("//rules/rust/remote:BUILD.tokio-postgres-0.5.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_postgres__0_7_0",
        url = "https://crates.io/api/v1/crates/tokio-postgres/0.7.0/download",
        type = "tar.gz",
        strip_prefix = "tokio-postgres-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-postgres-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_stream__0_1_2",
        url = "https://crates.io/api/v1/crates/tokio-stream/0.1.2/download",
        type = "tar.gz",
        strip_prefix = "tokio-stream-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.tokio-stream-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_2_0",
        url = "https://crates.io/api/v1/crates/tokio-util/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "tokio-util-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_3_1",
        url = "https://crates.io/api/v1/crates/tokio-util/0.3.1/download",
        type = "tar.gz",
        strip_prefix = "tokio-util-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_6_1",
        url = "https://crates.io/api/v1/crates/tokio-util/0.6.1/download",
        type = "tar.gz",
        strip_prefix = "tokio-util-0.6.1",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__toml__0_5_8",
        url = "https://crates.io/api/v1/crates/toml/0.5.8/download",
        type = "tar.gz",
        strip_prefix = "toml-0.5.8",
        build_file = Label("//rules/rust/remote:BUILD.toml-0.5.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing__0_1_22",
        url = "https://crates.io/api/v1/crates/tracing/0.1.22/download",
        type = "tar.gz",
        strip_prefix = "tracing-0.1.22",
        build_file = Label("//rules/rust/remote:BUILD.tracing-0.1.22.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_core__0_1_17",
        url = "https://crates.io/api/v1/crates/tracing-core/0.1.17/download",
        type = "tar.gz",
        strip_prefix = "tracing-core-0.1.17",
        build_file = Label("//rules/rust/remote:BUILD.tracing-core-0.1.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_futures__0_2_4",
        url = "https://crates.io/api/v1/crates/tracing-futures/0.2.4/download",
        type = "tar.gz",
        strip_prefix = "tracing-futures-0.2.4",
        build_file = Label("//rules/rust/remote:BUILD.tracing-futures-0.2.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__traitobject__0_1_0",
        url = "https://crates.io/api/v1/crates/traitobject/0.1.0/download",
        type = "tar.gz",
        strip_prefix = "traitobject-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.traitobject-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__trust_dns_proto__0_19_6",
        url = "https://crates.io/api/v1/crates/trust-dns-proto/0.19.6/download",
        type = "tar.gz",
        strip_prefix = "trust-dns-proto-0.19.6",
        build_file = Label("//rules/rust/remote:BUILD.trust-dns-proto-0.19.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__trust_dns_resolver__0_19_6",
        url = "https://crates.io/api/v1/crates/trust-dns-resolver/0.19.6/download",
        type = "tar.gz",
        strip_prefix = "trust-dns-resolver-0.19.6",
        build_file = Label("//rules/rust/remote:BUILD.trust-dns-resolver-0.19.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__typemap__0_3_3",
        url = "https://crates.io/api/v1/crates/typemap/0.3.3/download",
        type = "tar.gz",
        strip_prefix = "typemap-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.typemap-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__typenum__1_12_0",
        url = "https://crates.io/api/v1/crates/typenum/1.12.0/download",
        type = "tar.gz",
        strip_prefix = "typenum-1.12.0",
        build_file = Label("//rules/rust/remote:BUILD.typenum-1.12.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_bidi__0_3_4",
        url = "https://crates.io/api/v1/crates/unicode-bidi/0.3.4/download",
        type = "tar.gz",
        strip_prefix = "unicode-bidi-0.3.4",
        build_file = Label("//rules/rust/remote:BUILD.unicode-bidi-0.3.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_normalization__0_1_16",
        url = "https://crates.io/api/v1/crates/unicode-normalization/0.1.16/download",
        type = "tar.gz",
        strip_prefix = "unicode-normalization-0.1.16",
        build_file = Label("//rules/rust/remote:BUILD.unicode-normalization-0.1.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_segmentation__1_7_1",
        url = "https://crates.io/api/v1/crates/unicode-segmentation/1.7.1/download",
        type = "tar.gz",
        strip_prefix = "unicode-segmentation-1.7.1",
        build_file = Label("//rules/rust/remote:BUILD.unicode-segmentation-1.7.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_width__0_1_8",
        url = "https://crates.io/api/v1/crates/unicode-width/0.1.8/download",
        type = "tar.gz",
        strip_prefix = "unicode-width-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.unicode-width-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_xid__0_2_1",
        url = "https://crates.io/api/v1/crates/unicode-xid/0.2.1/download",
        type = "tar.gz",
        strip_prefix = "unicode-xid-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.unicode-xid-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unix_socket__0_5_0",
        url = "https://crates.io/api/v1/crates/unix_socket/0.5.0/download",
        type = "tar.gz",
        strip_prefix = "unix_socket-0.5.0",
        build_file = Label("//rules/rust/remote:BUILD.unix_socket-0.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unsafe_any__0_4_2",
        url = "https://crates.io/api/v1/crates/unsafe-any/0.4.2/download",
        type = "tar.gz",
        strip_prefix = "unsafe-any-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.unsafe-any-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__url__2_2_0",
        url = "https://crates.io/api/v1/crates/url/2.2.0/download",
        type = "tar.gz",
        strip_prefix = "url-2.2.0",
        build_file = Label("//rules/rust/remote:BUILD.url-2.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__urlparse__0_7_3",
        url = "https://crates.io/api/v1/crates/urlparse/0.7.3/download",
        type = "tar.gz",
        strip_prefix = "urlparse-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.urlparse-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__utf8_ranges__1_0_4",
        url = "https://crates.io/api/v1/crates/utf8-ranges/1.0.4/download",
        type = "tar.gz",
        strip_prefix = "utf8-ranges-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.utf8-ranges-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__uuid__0_8_2",
        url = "https://crates.io/api/v1/crates/uuid/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "uuid-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.uuid-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__vec_map__0_8_2",
        url = "https://crates.io/api/v1/crates/vec_map/0.8.2/download",
        type = "tar.gz",
        strip_prefix = "vec_map-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.vec_map-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__version_check__0_9_2",
        url = "https://crates.io/api/v1/crates/version_check/0.9.2/download",
        type = "tar.gz",
        strip_prefix = "version_check-0.9.2",
        build_file = Label("//rules/rust/remote:BUILD.version_check-0.9.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__void__1_0_2",
        url = "https://crates.io/api/v1/crates/void/1.0.2/download",
        type = "tar.gz",
        strip_prefix = "void-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.void-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wait_timeout__0_2_0",
        url = "https://crates.io/api/v1/crates/wait-timeout/0.2.0/download",
        type = "tar.gz",
        strip_prefix = "wait-timeout-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.wait-timeout-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__walkdir__2_3_1",
        url = "https://crates.io/api/v1/crates/walkdir/2.3.1/download",
        type = "tar.gz",
        strip_prefix = "walkdir-2.3.1",
        build_file = Label("//rules/rust/remote:BUILD.walkdir-2.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasi__0_10_1_wasi_snapshot_preview1",
        url = "https://crates.io/api/v1/crates/wasi/0.10.1+wasi-snapshot-preview1/download",
        type = "tar.gz",
        strip_prefix = "wasi-0.10.1+wasi-snapshot-preview1",
        build_file = Label("//rules/rust/remote:BUILD.wasi-0.10.1+wasi-snapshot-preview1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasi__0_9_0_wasi_snapshot_preview1",
        url = "https://crates.io/api/v1/crates/wasi/0.9.0+wasi-snapshot-preview1/download",
        type = "tar.gz",
        strip_prefix = "wasi-0.9.0+wasi-snapshot-preview1",
        build_file = Label("//rules/rust/remote:BUILD.wasi-0.9.0+wasi-snapshot-preview1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen__0_2_69",
        url = "https://crates.io/api/v1/crates/wasm-bindgen/0.2.69/download",
        type = "tar.gz",
        strip_prefix = "wasm-bindgen-0.2.69",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-0.2.69.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_backend__0_2_69",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-backend/0.2.69/download",
        type = "tar.gz",
        strip_prefix = "wasm-bindgen-backend-0.2.69",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-backend-0.2.69.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_macro__0_2_69",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-macro/0.2.69/download",
        type = "tar.gz",
        strip_prefix = "wasm-bindgen-macro-0.2.69",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-macro-0.2.69.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_macro_support__0_2_69",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-macro-support/0.2.69/download",
        type = "tar.gz",
        strip_prefix = "wasm-bindgen-macro-support-0.2.69",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-macro-support-0.2.69.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_shared__0_2_69",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-shared/0.2.69/download",
        type = "tar.gz",
        strip_prefix = "wasm-bindgen-shared-0.2.69",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-shared-0.2.69.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__web_sys__0_3_46",
        url = "https://crates.io/api/v1/crates/web-sys/0.3.46/download",
        type = "tar.gz",
        strip_prefix = "web-sys-0.3.46",
        build_file = Label("//rules/rust/remote:BUILD.web-sys-0.3.46.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__widestring__0_4_3",
        url = "https://crates.io/api/v1/crates/widestring/0.4.3/download",
        type = "tar.gz",
        strip_prefix = "widestring-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.widestring-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi__0_2_8",
        url = "https://crates.io/api/v1/crates/winapi/0.2.8/download",
        type = "tar.gz",
        strip_prefix = "winapi-0.2.8",
        build_file = Label("//rules/rust/remote:BUILD.winapi-0.2.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi__0_3_9",
        url = "https://crates.io/api/v1/crates/winapi/0.3.9/download",
        type = "tar.gz",
        strip_prefix = "winapi-0.3.9",
        build_file = Label("//rules/rust/remote:BUILD.winapi-0.3.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_build__0_1_1",
        url = "https://crates.io/api/v1/crates/winapi-build/0.1.1/download",
        type = "tar.gz",
        strip_prefix = "winapi-build-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.winapi-build-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_i686_pc_windows_gnu__0_4_0",
        url = "https://crates.io/api/v1/crates/winapi-i686-pc-windows-gnu/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "winapi-i686-pc-windows-gnu-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.winapi-i686-pc-windows-gnu-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_util__0_1_5",
        url = "https://crates.io/api/v1/crates/winapi-util/0.1.5/download",
        type = "tar.gz",
        strip_prefix = "winapi-util-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.winapi-util-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_x86_64_pc_windows_gnu__0_4_0",
        url = "https://crates.io/api/v1/crates/winapi-x86_64-pc-windows-gnu/0.4.0/download",
        type = "tar.gz",
        strip_prefix = "winapi-x86_64-pc-windows-gnu-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.winapi-x86_64-pc-windows-gnu-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winreg__0_6_2",
        url = "https://crates.io/api/v1/crates/winreg/0.6.2/download",
        type = "tar.gz",
        strip_prefix = "winreg-0.6.2",
        build_file = Label("//rules/rust/remote:BUILD.winreg-0.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ws2_32_sys__0_2_1",
        url = "https://crates.io/api/v1/crates/ws2_32-sys/0.2.1/download",
        type = "tar.gz",
        strip_prefix = "ws2_32-sys-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.ws2_32-sys-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__xattr__0_2_2",
        url = "https://crates.io/api/v1/crates/xattr/0.2.2/download",
        type = "tar.gz",
        strip_prefix = "xattr-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.xattr-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__yaml_rust__0_4_5",
        url = "https://crates.io/api/v1/crates/yaml-rust/0.4.5/download",
        type = "tar.gz",
        strip_prefix = "yaml-rust-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.yaml-rust-0.4.5.bazel"),
    )
