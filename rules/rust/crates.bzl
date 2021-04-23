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
        sha256 = "1be241f88f3b1e7e9a3fbe3b5a8a0f6915b5a1d7ee0d9a248d3376d01068cc60",
        strip_prefix = "actix-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_codec__0_2_0",
        url = "https://crates.io/api/v1/crates/actix-codec/0.2.0/download",
        type = "tar.gz",
        sha256 = "09e55f0a5c2ca15795035d90c46bd0e73a5123b72f68f12596d6ba5282051380",
        strip_prefix = "actix-codec-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-codec-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_codec__0_3_0",
        url = "https://crates.io/api/v1/crates/actix-codec/0.3.0/download",
        type = "tar.gz",
        sha256 = "78d1833b3838dbe990df0f1f87baf640cf6146e898166afe401839d1b001e570",
        strip_prefix = "actix-codec-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-codec-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_connect__2_0_0",
        url = "https://crates.io/api/v1/crates/actix-connect/2.0.0/download",
        type = "tar.gz",
        sha256 = "177837a10863f15ba8d3ae3ec12fac1099099529ed20083a27fdfe247381d0dc",
        strip_prefix = "actix-connect-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-connect-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_cors__0_5_4",
        url = "https://crates.io/api/v1/crates/actix-cors/0.5.4/download",
        type = "tar.gz",
        sha256 = "36b133d8026a9f209a9aeeeacd028e7451bcca975f592881b305d37983f303d7",
        strip_prefix = "actix-cors-0.5.4",
        build_file = Label("//rules/rust/remote:BUILD.actix-cors-0.5.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_http__2_2_0",
        url = "https://crates.io/api/v1/crates/actix-http/2.2.0/download",
        type = "tar.gz",
        sha256 = "452299e87817ae5673910e53c243484ca38be3828db819b6011736fc6982e874",
        strip_prefix = "actix-http-2.2.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-http-2.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_macros__0_1_3",
        url = "https://crates.io/api/v1/crates/actix-macros/0.1.3/download",
        type = "tar.gz",
        sha256 = "b4ca8ce00b267af8ccebbd647de0d61e0674b6e61185cc7a592ff88772bed655",
        strip_prefix = "actix-macros-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.actix-macros-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_router__0_2_7",
        url = "https://crates.io/api/v1/crates/actix-router/0.2.7/download",
        type = "tar.gz",
        sha256 = "2ad299af73649e1fc893e333ccf86f377751eb95ff875d095131574c6f43452c",
        strip_prefix = "actix-router-0.2.7",
        build_file = Label("//rules/rust/remote:BUILD.actix-router-0.2.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_rt__1_1_1",
        url = "https://crates.io/api/v1/crates/actix-rt/1.1.1/download",
        type = "tar.gz",
        sha256 = "143fcc2912e0d1de2bcf4e2f720d2a60c28652ab4179685a1ee159e0fb3db227",
        strip_prefix = "actix-rt-1.1.1",
        build_file = Label("//rules/rust/remote:BUILD.actix-rt-1.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_server__1_0_4",
        url = "https://crates.io/api/v1/crates/actix-server/1.0.4/download",
        type = "tar.gz",
        sha256 = "45407e6e672ca24784baa667c5d32ef109ccdd8d5e0b5ebb9ef8a67f4dfb708e",
        strip_prefix = "actix-server-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.actix-server-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_service__1_0_6",
        url = "https://crates.io/api/v1/crates/actix-service/1.0.6/download",
        type = "tar.gz",
        sha256 = "0052435d581b5be835d11f4eb3bce417c8af18d87ddf8ace99f8e67e595882bb",
        strip_prefix = "actix-service-1.0.6",
        build_file = Label("//rules/rust/remote:BUILD.actix-service-1.0.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_testing__1_0_1",
        url = "https://crates.io/api/v1/crates/actix-testing/1.0.1/download",
        type = "tar.gz",
        sha256 = "47239ca38799ab74ee6a8a94d1ce857014b2ac36f242f70f3f75a66f691e791c",
        strip_prefix = "actix-testing-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.actix-testing-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_threadpool__0_3_3",
        url = "https://crates.io/api/v1/crates/actix-threadpool/0.3.3/download",
        type = "tar.gz",
        sha256 = "d209f04d002854b9afd3743032a27b066158817965bf5d036824d19ac2cc0e30",
        strip_prefix = "actix-threadpool-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.actix-threadpool-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_tls__2_0_0",
        url = "https://crates.io/api/v1/crates/actix-tls/2.0.0/download",
        type = "tar.gz",
        sha256 = "24789b7d7361cf5503a504ebe1c10806896f61e96eca9a7350e23001aca715fb",
        strip_prefix = "actix-tls-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-tls-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_utils__1_0_6",
        url = "https://crates.io/api/v1/crates/actix-utils/1.0.6/download",
        type = "tar.gz",
        sha256 = "fcf8f5631bf01adec2267808f00e228b761c60c0584cc9fa0b5364f41d147f4e",
        strip_prefix = "actix-utils-1.0.6",
        build_file = Label("//rules/rust/remote:BUILD.actix-utils-1.0.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_utils__2_0_0",
        url = "https://crates.io/api/v1/crates/actix-utils/2.0.0/download",
        type = "tar.gz",
        sha256 = "2e9022dec56632d1d7979e59af14f0597a28a830a9c1c7fec8b2327eb9f16b5a",
        strip_prefix = "actix-utils-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-utils-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_web__3_3_2",
        url = "https://crates.io/api/v1/crates/actix-web/3.3.2/download",
        type = "tar.gz",
        sha256 = "e641d4a172e7faa0862241a20ff4f1f5ab0ab7c279f00c2d4587b77483477b86",
        strip_prefix = "actix-web-3.3.2",
        build_file = Label("//rules/rust/remote:BUILD.actix-web-3.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_web_codegen__0_4_0",
        url = "https://crates.io/api/v1/crates/actix-web-codegen/0.4.0/download",
        type = "tar.gz",
        sha256 = "ad26f77093333e0e7c6ffe54ebe3582d908a104e448723eec6d43d08b07143fb",
        strip_prefix = "actix-web-codegen-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.actix-web-codegen-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__actix_derive__0_5_0",
        url = "https://crates.io/api/v1/crates/actix_derive/0.5.0/download",
        type = "tar.gz",
        sha256 = "b95aceadaf327f18f0df5962fedc1bde2f870566a0b9f65c89508a3b1f79334c",
        strip_prefix = "actix_derive-0.5.0",
        build_file = Label("//rules/rust/remote:BUILD.actix_derive-0.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__addr2line__0_14_1",
        url = "https://crates.io/api/v1/crates/addr2line/0.14.1/download",
        type = "tar.gz",
        sha256 = "a55f82cfe485775d02112886f4169bde0c5894d75e79ead7eafe7e40a25e45f7",
        strip_prefix = "addr2line-0.14.1",
        build_file = Label("//rules/rust/remote:BUILD.addr2line-0.14.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__adler__1_0_2",
        url = "https://crates.io/api/v1/crates/adler/1.0.2/download",
        type = "tar.gz",
        sha256 = "f26201604c87b1e01bd3d98f8d5d9a8fcbb815e8cedb41ffccbeb4bf593a35fe",
        strip_prefix = "adler-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.adler-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ahash__0_4_7",
        url = "https://crates.io/api/v1/crates/ahash/0.4.7/download",
        type = "tar.gz",
        sha256 = "739f4a8db6605981345c5654f3a85b056ce52f37a39d34da03f25bf2151ea16e",
        strip_prefix = "ahash-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.ahash-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__aho_corasick__0_7_15",
        url = "https://crates.io/api/v1/crates/aho-corasick/0.7.15/download",
        type = "tar.gz",
        sha256 = "7404febffaa47dac81aa44dba71523c9d069b1bdc50a77db41195149e17f68e5",
        strip_prefix = "aho-corasick-0.7.15",
        build_file = Label("//rules/rust/remote:BUILD.aho-corasick-0.7.15.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__alloc_no_stdlib__2_0_1",
        url = "https://crates.io/api/v1/crates/alloc-no-stdlib/2.0.1/download",
        type = "tar.gz",
        sha256 = "5192ec435945d87bc2f70992b4d818154b5feede43c09fb7592146374eac90a6",
        strip_prefix = "alloc-no-stdlib-2.0.1",
        build_file = Label("//rules/rust/remote:BUILD.alloc-no-stdlib-2.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__alloc_stdlib__0_2_1",
        url = "https://crates.io/api/v1/crates/alloc-stdlib/0.2.1/download",
        type = "tar.gz",
        sha256 = "697ed7edc0f1711de49ce108c541623a0af97c6c60b2f6e2b65229847ac843c2",
        strip_prefix = "alloc-stdlib-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.alloc-stdlib-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ansi_term__0_11_0",
        url = "https://crates.io/api/v1/crates/ansi_term/0.11.0/download",
        type = "tar.gz",
        sha256 = "ee49baf6cb617b853aa8d93bf420db2383fab46d314482ca2803b40d5fde979b",
        strip_prefix = "ansi_term-0.11.0",
        build_file = Label("//rules/rust/remote:BUILD.ansi_term-0.11.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__antidote__1_0_0",
        url = "https://crates.io/api/v1/crates/antidote/1.0.0/download",
        type = "tar.gz",
        sha256 = "34fde25430d87a9388dadbe6e34d7f72a462c8b43ac8d309b42b0a8505d7e2a5",
        strip_prefix = "antidote-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.antidote-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arc_swap__0_4_8",
        url = "https://crates.io/api/v1/crates/arc-swap/0.4.8/download",
        type = "tar.gz",
        sha256 = "dabe5a181f83789739c194cbe5a897dde195078fac08568d09221fd6137a7ba8",
        strip_prefix = "arc-swap-0.4.8",
        build_file = Label("//rules/rust/remote:BUILD.arc-swap-0.4.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arc_swap__1_2_0",
        url = "https://crates.io/api/v1/crates/arc-swap/1.2.0/download",
        type = "tar.gz",
        sha256 = "d4d7d63395147b81a9e570bcc6243aaf71c017bd666d4909cfef0085bdda8d73",
        strip_prefix = "arc-swap-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.arc-swap-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__arrayvec__0_5_2",
        url = "https://crates.io/api/v1/crates/arrayvec/0.5.2/download",
        type = "tar.gz",
        sha256 = "23b62fc65de8e4e7f52534fb52b0f3ed04746ae267519eef2a83941e8085068b",
        strip_prefix = "arrayvec-0.5.2",
        build_file = Label("//rules/rust/remote:BUILD.arrayvec-0.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__async_trait__0_1_50",
        url = "https://crates.io/api/v1/crates/async-trait/0.1.50/download",
        type = "tar.gz",
        sha256 = "0b98e84bbb4cbcdd97da190ba0c58a1bb0de2c1fdf67d159e192ed766aeca722",
        strip_prefix = "async-trait-0.1.50",
        build_file = Label("//rules/rust/remote:BUILD.async-trait-0.1.50.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__atomicwrites__0_2_5",
        url = "https://crates.io/api/v1/crates/atomicwrites/0.2.5/download",
        type = "tar.gz",
        sha256 = "6a2baf2feb820299c53c7ad1cc4f5914a220a1cb76d7ce321d2522a94b54651f",
        strip_prefix = "atomicwrites-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.atomicwrites-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__atty__0_2_14",
        url = "https://crates.io/api/v1/crates/atty/0.2.14/download",
        type = "tar.gz",
        sha256 = "d9b39be18770d11421cdb1b9947a45dd3f37e93092cbf377614828a319d5fee8",
        strip_prefix = "atty-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.atty-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__autocfg__1_0_1",
        url = "https://crates.io/api/v1/crates/autocfg/1.0.1/download",
        type = "tar.gz",
        sha256 = "cdb031dd78e28731d87d56cc8ffef4a8f36ca26c38fe2de700543e627f8a464a",
        strip_prefix = "autocfg-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.autocfg-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__awc__2_0_3",
        url = "https://crates.io/api/v1/crates/awc/2.0.3/download",
        type = "tar.gz",
        sha256 = "b381e490e7b0cfc37ebc54079b0413d8093ef43d14a4e4747083f7fa47a9e691",
        strip_prefix = "awc-2.0.3",
        build_file = Label("//rules/rust/remote:BUILD.awc-2.0.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__backtrace__0_3_56",
        url = "https://crates.io/api/v1/crates/backtrace/0.3.56/download",
        type = "tar.gz",
        sha256 = "9d117600f438b1707d4e4ae15d3595657288f8235a0eb593e80ecc98ab34e1bc",
        strip_prefix = "backtrace-0.3.56",
        build_file = Label("//rules/rust/remote:BUILD.backtrace-0.3.56.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base_x__0_2_8",
        url = "https://crates.io/api/v1/crates/base-x/0.2.8/download",
        type = "tar.gz",
        sha256 = "a4521f3e3d031370679b3b140beb36dfe4801b09ac77e30c61941f97df3ef28b",
        strip_prefix = "base-x-0.2.8",
        build_file = Label("//rules/rust/remote:BUILD.base-x-0.2.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_12_3",
        url = "https://crates.io/api/v1/crates/base64/0.12.3/download",
        type = "tar.gz",
        sha256 = "3441f0f7b02788e948e47f457ca01f1d7e6d92c693bc132c22b087d3141c03ff",
        strip_prefix = "base64-0.12.3",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.12.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_13_0",
        url = "https://crates.io/api/v1/crates/base64/0.13.0/download",
        type = "tar.gz",
        sha256 = "904dfeac50f3cdaba28fc6f57fdcddb75f49ed61346676a78c4ffe55877802fd",
        strip_prefix = "base64-0.13.0",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_9_3",
        url = "https://crates.io/api/v1/crates/base64/0.9.3/download",
        type = "tar.gz",
        sha256 = "489d6c0ed21b11d038c31b6ceccca973e65d73ba3bd8ecb9a2babf5546164643",
        strip_prefix = "base64-0.9.3",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.9.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bb8__0_4_2",
        url = "https://crates.io/api/v1/crates/bb8/0.4.2/download",
        type = "tar.gz",
        sha256 = "374bba43fc924d90393ee7768e6f75d223a98307a488fe5bc34b66c3e96932a6",
        strip_prefix = "bb8-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.bb8-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bb8_postgres__0_4_0",
        url = "https://crates.io/api/v1/crates/bb8-postgres/0.4.0/download",
        type = "tar.gz",
        sha256 = "39a233af6ea3952e20d01863c87b4f6689b2f806249688b0908b5f02d4fa41ac",
        strip_prefix = "bb8-postgres-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.bb8-postgres-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bincode__1_3_3",
        url = "https://crates.io/api/v1/crates/bincode/1.3.3/download",
        type = "tar.gz",
        sha256 = "b1f45e9417d87227c7a56d22e471c6206462cba514c7590c09aff4cf6d1ddcad",
        strip_prefix = "bincode-1.3.3",
        build_file = Label("//rules/rust/remote:BUILD.bincode-1.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bit_set__0_5_2",
        url = "https://crates.io/api/v1/crates/bit-set/0.5.2/download",
        type = "tar.gz",
        sha256 = "6e11e16035ea35e4e5997b393eacbf6f63983188f7a2ad25bfb13465f5ad59de",
        strip_prefix = "bit-set-0.5.2",
        build_file = Label("//rules/rust/remote:BUILD.bit-set-0.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bit_vec__0_6_3",
        url = "https://crates.io/api/v1/crates/bit-vec/0.6.3/download",
        type = "tar.gz",
        sha256 = "349f9b6a179ed607305526ca489b34ad0a41aed5f7980fa90eb03160b69598fb",
        strip_prefix = "bit-vec-0.6.3",
        build_file = Label("//rules/rust/remote:BUILD.bit-vec-0.6.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bitflags__1_2_1",
        url = "https://crates.io/api/v1/crates/bitflags/1.2.1/download",
        type = "tar.gz",
        sha256 = "cf1de2fe8c75bc145a2f577add951f8134889b4795d47466a54a5c846d691693",
        strip_prefix = "bitflags-1.2.1",
        build_file = Label("//rules/rust/remote:BUILD.bitflags-1.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bitpacking__0_8_2",
        url = "https://crates.io/api/v1/crates/bitpacking/0.8.2/download",
        type = "tar.gz",
        sha256 = "3744aff20a3437a99ebc0bb7733e9e60c7bf590478c9b897e95b38d57e5acb68",
        strip_prefix = "bitpacking-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.bitpacking-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__block_buffer__0_9_0",
        url = "https://crates.io/api/v1/crates/block-buffer/0.9.0/download",
        type = "tar.gz",
        sha256 = "4152116fd6e9dadb291ae18fc1ec3575ed6d84c29642d97890f4b4a3417297e4",
        strip_prefix = "block-buffer-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.block-buffer-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__brotli__3_3_0",
        url = "https://crates.io/api/v1/crates/brotli/3.3.0/download",
        type = "tar.gz",
        sha256 = "7f29919120f08613aadcd4383764e00526fc9f18b6c0895814faeed0dd78613e",
        strip_prefix = "brotli-3.3.0",
        build_file = Label("//rules/rust/remote:BUILD.brotli-3.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__brotli_decompressor__2_3_1",
        url = "https://crates.io/api/v1/crates/brotli-decompressor/2.3.1/download",
        type = "tar.gz",
        sha256 = "1052e1c3b8d4d80eb84a8b94f0a1498797b5fb96314c001156a1c761940ef4ec",
        strip_prefix = "brotli-decompressor-2.3.1",
        build_file = Label("//rules/rust/remote:BUILD.brotli-decompressor-2.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bstr__0_2_15",
        url = "https://crates.io/api/v1/crates/bstr/0.2.15/download",
        type = "tar.gz",
        sha256 = "a40b47ad93e1a5404e6c18dec46b628214fee441c70f4ab5d6942142cc268a3d",
        strip_prefix = "bstr-0.2.15",
        build_file = Label("//rules/rust/remote:BUILD.bstr-0.2.15.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bumpalo__3_6_1",
        url = "https://crates.io/api/v1/crates/bumpalo/3.6.1/download",
        type = "tar.gz",
        sha256 = "63396b8a4b9de3f4fdfb320ab6080762242f66a8ef174c49d8e19b674db4cdbe",
        strip_prefix = "bumpalo-3.6.1",
        build_file = Label("//rules/rust/remote:BUILD.bumpalo-3.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__byteorder__1_4_3",
        url = "https://crates.io/api/v1/crates/byteorder/1.4.3/download",
        type = "tar.gz",
        sha256 = "14c189c53d098945499cdfa7ecc63567cf3886b3332b312a5b4585d8d3a6a610",
        strip_prefix = "byteorder-1.4.3",
        build_file = Label("//rules/rust/remote:BUILD.byteorder-1.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytes__0_5_6",
        url = "https://crates.io/api/v1/crates/bytes/0.5.6/download",
        type = "tar.gz",
        sha256 = "0e4cec68f03f32e44924783795810fa50a7035d8c8ebe78580ad7e6c703fba38",
        strip_prefix = "bytes-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.bytes-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytes__1_0_1",
        url = "https://crates.io/api/v1/crates/bytes/1.0.1/download",
        type = "tar.gz",
        sha256 = "b700ce4376041dcd0a327fd0097c41095743c4c8af8887265942faf1100bd040",
        strip_prefix = "bytes-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.bytes-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytestring__1_0_0",
        url = "https://crates.io/api/v1/crates/bytestring/1.0.0/download",
        type = "tar.gz",
        sha256 = "90706ba19e97b90786e19dc0d5e2abd80008d99d4c0c5d1ad0b5e72cec7c494d",
        strip_prefix = "bytestring-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.bytestring-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cast__0_2_5",
        url = "https://crates.io/api/v1/crates/cast/0.2.5/download",
        type = "tar.gz",
        sha256 = "cc38c385bfd7e444464011bb24820f40dd1c76bcdfa1b78611cb7c2e5cafab75",
        strip_prefix = "cast-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.cast-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cc__1_0_67",
        url = "https://crates.io/api/v1/crates/cc/1.0.67/download",
        type = "tar.gz",
        sha256 = "e3c69b077ad434294d3ce9f1f6143a2a4b89a8a2d54ef813d85003a4fd1137fd",
        strip_prefix = "cc-1.0.67",
        build_file = Label("//rules/rust/remote:BUILD.cc-1.0.67.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__census__0_4_0",
        url = "https://crates.io/api/v1/crates/census/0.4.0/download",
        type = "tar.gz",
        sha256 = "5927edd8345aef08578bcbb4aea7314f340d80c7f4931f99fbeb40b99d8f5060",
        strip_prefix = "census-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.census-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cfg_if__0_1_10",
        url = "https://crates.io/api/v1/crates/cfg-if/0.1.10/download",
        type = "tar.gz",
        sha256 = "4785bdd1c96b2a846b2bd7cc02e86b6b3dbf14e7e53446c4f54c92a361040822",
        strip_prefix = "cfg-if-0.1.10",
        build_file = Label("//rules/rust/remote:BUILD.cfg-if-0.1.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cfg_if__1_0_0",
        url = "https://crates.io/api/v1/crates/cfg-if/1.0.0/download",
        type = "tar.gz",
        sha256 = "baf1de4339761588bc0619e3cbc0120ee582ebb74b53b4efbf79117bd2da40fd",
        strip_prefix = "cfg-if-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.cfg-if-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__chrono__0_4_19",
        url = "https://crates.io/api/v1/crates/chrono/0.4.19/download",
        type = "tar.gz",
        sha256 = "670ad68c9088c2a963aaa298cb369688cf3f9465ce5e2d4ca10e6e0098a1ce73",
        strip_prefix = "chrono-0.4.19",
        build_file = Label("//rules/rust/remote:BUILD.chrono-0.4.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__clap__2_33_3",
        url = "https://crates.io/api/v1/crates/clap/2.33.3/download",
        type = "tar.gz",
        sha256 = "37e58ac78573c40708d45522f0d80fa2f01cc4f9b4e2bf749807255454312002",
        strip_prefix = "clap-2.33.3",
        build_file = Label("//rules/rust/remote:BUILD.clap-2.33.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cloudabi__0_0_3",
        url = "https://crates.io/api/v1/crates/cloudabi/0.0.3/download",
        type = "tar.gz",
        sha256 = "ddfc5b9aa5d4507acaf872de71051dfd0e309860e88966e1051e462a077aac4f",
        strip_prefix = "cloudabi-0.0.3",
        build_file = Label("//rules/rust/remote:BUILD.cloudabi-0.0.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__colored__2_0_0",
        url = "https://crates.io/api/v1/crates/colored/2.0.0/download",
        type = "tar.gz",
        sha256 = "b3616f750b84d8f0de8a58bda93e08e2a81ad3f523089b05f1dffecab48c6cbd",
        strip_prefix = "colored-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.colored-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__combine__4_5_2",
        url = "https://crates.io/api/v1/crates/combine/4.5.2/download",
        type = "tar.gz",
        sha256 = "cc4369b5e4c0cddf64ad8981c0111e7df4f7078f4d6ba98fb31f2e17c4c57b7e",
        strip_prefix = "combine-4.5.2",
        build_file = Label("//rules/rust/remote:BUILD.combine-4.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__config__0_10_1",
        url = "https://crates.io/api/v1/crates/config/0.10.1/download",
        type = "tar.gz",
        sha256 = "19b076e143e1d9538dde65da30f8481c2a6c44040edb8e02b9bf1351edb92ce3",
        strip_prefix = "config-0.10.1",
        build_file = Label("//rules/rust/remote:BUILD.config-0.10.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__config__0_11_0",
        url = "https://crates.io/api/v1/crates/config/0.11.0/download",
        type = "tar.gz",
        sha256 = "1b1b9d958c2b1368a663f05538fc1b5975adce1e19f435acceae987aceeeb369",
        strip_prefix = "config-0.11.0",
        build_file = Label("//rules/rust/remote:BUILD.config-0.11.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__const_fn__0_4_7",
        url = "https://crates.io/api/v1/crates/const_fn/0.4.7/download",
        type = "tar.gz",
        sha256 = "402da840495de3f976eaefc3485b7f5eb5b0bf9761f9a47be27fe975b3b8c2ec",
        strip_prefix = "const_fn-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.const_fn-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__convert_case__0_4_0",
        url = "https://crates.io/api/v1/crates/convert_case/0.4.0/download",
        type = "tar.gz",
        sha256 = "6245d59a3e82a7fc217c5828a6692dbc6dfb63a0c8c90495621f7b9d79704a0e",
        strip_prefix = "convert_case-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.convert_case-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cookie__0_14_4",
        url = "https://crates.io/api/v1/crates/cookie/0.14.4/download",
        type = "tar.gz",
        sha256 = "03a5d7b21829bc7b4bf4754a978a241ae54ea55a40f92bb20216e54096f4b951",
        strip_prefix = "cookie-0.14.4",
        build_file = Label("//rules/rust/remote:BUILD.cookie-0.14.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__copyless__0_1_5",
        url = "https://crates.io/api/v1/crates/copyless/0.1.5/download",
        type = "tar.gz",
        sha256 = "a2df960f5d869b2dd8532793fde43eb5427cceb126c929747a26823ab0eeb536",
        strip_prefix = "copyless-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.copyless-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cpuid_bool__0_1_2",
        url = "https://crates.io/api/v1/crates/cpuid-bool/0.1.2/download",
        type = "tar.gz",
        sha256 = "8aebca1129a03dc6dc2b127edd729435bbc4a37e1d5f4d7513165089ceb02634",
        strip_prefix = "cpuid-bool-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.cpuid-bool-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crc32fast__1_2_1",
        url = "https://crates.io/api/v1/crates/crc32fast/1.2.1/download",
        type = "tar.gz",
        sha256 = "81156fece84ab6a9f2afdb109ce3ae577e42b1228441eded99bd77f627953b1a",
        strip_prefix = "crc32fast-1.2.1",
        build_file = Label("//rules/rust/remote:BUILD.crc32fast-1.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__criterion__0_3_4",
        url = "https://crates.io/api/v1/crates/criterion/0.3.4/download",
        type = "tar.gz",
        sha256 = "ab327ed7354547cc2ef43cbe20ef68b988e70b4b593cbd66a2a61733123a3d23",
        strip_prefix = "criterion-0.3.4",
        build_file = Label("//rules/rust/remote:BUILD.criterion-0.3.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__criterion_plot__0_4_3",
        url = "https://crates.io/api/v1/crates/criterion-plot/0.4.3/download",
        type = "tar.gz",
        sha256 = "e022feadec601fba1649cfa83586381a4ad31c6bf3a9ab7d408118b05dd9889d",
        strip_prefix = "criterion-plot-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.criterion-plot-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam__0_7_3",
        url = "https://crates.io/api/v1/crates/crossbeam/0.7.3/download",
        type = "tar.gz",
        sha256 = "69323bff1fb41c635347b8ead484a5ca6c3f11914d784170b158d8449ab07f8e",
        strip_prefix = "crossbeam-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_channel__0_4_4",
        url = "https://crates.io/api/v1/crates/crossbeam-channel/0.4.4/download",
        type = "tar.gz",
        sha256 = "b153fe7cbef478c567df0f972e02e6d736db11affe43dfc9c56a9374d1adfb87",
        strip_prefix = "crossbeam-channel-0.4.4",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-channel-0.4.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_channel__0_5_1",
        url = "https://crates.io/api/v1/crates/crossbeam-channel/0.5.1/download",
        type = "tar.gz",
        sha256 = "06ed27e177f16d65f0f0c22a213e17c696ace5dd64b14258b52f9417ccb52db4",
        strip_prefix = "crossbeam-channel-0.5.1",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-channel-0.5.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_deque__0_7_3",
        url = "https://crates.io/api/v1/crates/crossbeam-deque/0.7.3/download",
        type = "tar.gz",
        sha256 = "9f02af974daeee82218205558e51ec8768b48cf524bd01d550abe5573a608285",
        strip_prefix = "crossbeam-deque-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-deque-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_deque__0_8_0",
        url = "https://crates.io/api/v1/crates/crossbeam-deque/0.8.0/download",
        type = "tar.gz",
        sha256 = "94af6efb46fef72616855b036a624cf27ba656ffc9be1b9a3c931cfc7749a9a9",
        strip_prefix = "crossbeam-deque-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-deque-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_epoch__0_8_2",
        url = "https://crates.io/api/v1/crates/crossbeam-epoch/0.8.2/download",
        type = "tar.gz",
        sha256 = "058ed274caafc1f60c4997b5fc07bf7dc7cca454af7c6e81edffe5f33f70dace",
        strip_prefix = "crossbeam-epoch-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-epoch-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_epoch__0_9_3",
        url = "https://crates.io/api/v1/crates/crossbeam-epoch/0.9.3/download",
        type = "tar.gz",
        sha256 = "2584f639eb95fea8c798496315b297cf81b9b58b6d30ab066a75455333cf4b12",
        strip_prefix = "crossbeam-epoch-0.9.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-epoch-0.9.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_queue__0_2_3",
        url = "https://crates.io/api/v1/crates/crossbeam-queue/0.2.3/download",
        type = "tar.gz",
        sha256 = "774ba60a54c213d409d5353bda12d49cd68d14e45036a285234c8d6f91f92570",
        strip_prefix = "crossbeam-queue-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-queue-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_utils__0_7_2",
        url = "https://crates.io/api/v1/crates/crossbeam-utils/0.7.2/download",
        type = "tar.gz",
        sha256 = "c3c7c73a2d1e9fc0886a08b93e98eb643461230d5f1925e4036204d5f2e261a8",
        strip_prefix = "crossbeam-utils-0.7.2",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-utils-0.7.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_utils__0_8_3",
        url = "https://crates.io/api/v1/crates/crossbeam-utils/0.8.3/download",
        type = "tar.gz",
        sha256 = "e7e9d99fa91428effe99c5c6d4634cdeba32b8cf784fc428a2a687f61a952c49",
        strip_prefix = "crossbeam-utils-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-utils-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crunchy__0_2_2",
        url = "https://crates.io/api/v1/crates/crunchy/0.2.2/download",
        type = "tar.gz",
        sha256 = "7a81dae078cea95a014a339291cec439d2f232ebe854a9d672b796c6afafa9b7",
        strip_prefix = "crunchy-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.crunchy-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crypto_mac__0_10_0",
        url = "https://crates.io/api/v1/crates/crypto-mac/0.10.0/download",
        type = "tar.gz",
        sha256 = "4857fd85a0c34b3c3297875b747c1e02e06b6a0ea32dd892d8192b9ce0813ea6",
        strip_prefix = "crypto-mac-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.crypto-mac-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crypto_mac__0_9_1",
        url = "https://crates.io/api/v1/crates/crypto-mac/0.9.1/download",
        type = "tar.gz",
        sha256 = "58bcd97a54c7ca5ce2f6eb16f6bede5b0ab5f0055fedc17d2f0b4466e21671ca",
        strip_prefix = "crypto-mac-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.crypto-mac-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__csv__1_1_6",
        url = "https://crates.io/api/v1/crates/csv/1.1.6/download",
        type = "tar.gz",
        sha256 = "22813a6dc45b335f9bade10bf7271dc477e81113e89eb251a0bc2a8a81c536e1",
        strip_prefix = "csv-1.1.6",
        build_file = Label("//rules/rust/remote:BUILD.csv-1.1.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__csv_core__0_1_10",
        url = "https://crates.io/api/v1/crates/csv-core/0.1.10/download",
        type = "tar.gz",
        sha256 = "2b2466559f260f48ad25fe6317b3c8dac77b5bdb5763ac7d9d6103530663bc90",
        strip_prefix = "csv-core-0.1.10",
        build_file = Label("//rules/rust/remote:BUILD.csv-core-0.1.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__deadpool__0_5_2",
        url = "https://crates.io/api/v1/crates/deadpool/0.5.2/download",
        type = "tar.gz",
        sha256 = "4aaff9a7a1de9893f4004fa08527b31cb2ae4121c44e053cf53f29203c73bd23",
        strip_prefix = "deadpool-0.5.2",
        build_file = Label("//rules/rust/remote:BUILD.deadpool-0.5.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__deadpool_postgres__0_5_6",
        url = "https://crates.io/api/v1/crates/deadpool-postgres/0.5.6/download",
        type = "tar.gz",
        sha256 = "faad41e7f93dd682108c72aec029e5bc6238e7df64c9d84832525d4033d2e726",
        strip_prefix = "deadpool-postgres-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.deadpool-postgres-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__derive_more__0_99_13",
        url = "https://crates.io/api/v1/crates/derive_more/0.99.13/download",
        type = "tar.gz",
        sha256 = "f82b1b72f1263f214c0f823371768776c4f5841b942c9883aa8e5ec584fd0ba6",
        strip_prefix = "derive_more-0.99.13",
        build_file = Label("//rules/rust/remote:BUILD.derive_more-0.99.13.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__digest__0_9_0",
        url = "https://crates.io/api/v1/crates/digest/0.9.0/download",
        type = "tar.gz",
        sha256 = "d3dd60d1080a57a05ab032377049e0591415d2b31afd7028356dbf3cc6dcb066",
        strip_prefix = "digest-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.digest-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dirs_next__2_0_0",
        url = "https://crates.io/api/v1/crates/dirs-next/2.0.0/download",
        type = "tar.gz",
        sha256 = "b98cf8ebf19c3d1b223e151f99a4f9f0690dca41414773390fc824184ac833e1",
        strip_prefix = "dirs-next-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.dirs-next-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dirs_sys_next__0_1_2",
        url = "https://crates.io/api/v1/crates/dirs-sys-next/0.1.2/download",
        type = "tar.gz",
        sha256 = "4ebda144c4fe02d1f7ea1a7d9641b6fc6b580adcfa024ae48797ecdeb6825b4d",
        strip_prefix = "dirs-sys-next-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.dirs-sys-next-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__discard__1_0_4",
        url = "https://crates.io/api/v1/crates/discard/1.0.4/download",
        type = "tar.gz",
        sha256 = "212d0f5754cb6769937f4501cc0e67f4f4483c8d2c3e1e922ee9edbe4ab4c7c0",
        strip_prefix = "discard-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.discard-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dotenv__0_15_0",
        url = "https://crates.io/api/v1/crates/dotenv/0.15.0/download",
        type = "tar.gz",
        sha256 = "77c90badedccf4105eca100756a0b1289e191f6fcbdadd3cee1d2f614f97da8f",
        strip_prefix = "dotenv-0.15.0",
        build_file = Label("//rules/rust/remote:BUILD.dotenv-0.15.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__downcast_rs__1_2_0",
        url = "https://crates.io/api/v1/crates/downcast-rs/1.2.0/download",
        type = "tar.gz",
        sha256 = "9ea835d29036a4087793836fa931b08837ad5e957da9e23886b29586fb9b6650",
        strip_prefix = "downcast-rs-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.downcast-rs-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dtoa__0_4_8",
        url = "https://crates.io/api/v1/crates/dtoa/0.4.8/download",
        type = "tar.gz",
        sha256 = "56899898ce76aaf4a0f24d914c97ea6ed976d42fec6ad33fcbb0a1103e07b2b0",
        strip_prefix = "dtoa-0.4.8",
        build_file = Label("//rules/rust/remote:BUILD.dtoa-0.4.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__either__1_6_1",
        url = "https://crates.io/api/v1/crates/either/1.6.1/download",
        type = "tar.gz",
        sha256 = "e78d4f1cc4ae33bbfc157ed5d5a5ef3bc29227303d595861deb238fcec4e9457",
        strip_prefix = "either-1.6.1",
        build_file = Label("//rules/rust/remote:BUILD.either-1.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__encoding_rs__0_8_28",
        url = "https://crates.io/api/v1/crates/encoding_rs/0.8.28/download",
        type = "tar.gz",
        sha256 = "80df024fbc5ac80f87dfef0d9f5209a252f2a497f7f42944cff24d8253cac065",
        strip_prefix = "encoding_rs-0.8.28",
        build_file = Label("//rules/rust/remote:BUILD.encoding_rs-0.8.28.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__enum_as_inner__0_3_3",
        url = "https://crates.io/api/v1/crates/enum-as-inner/0.3.3/download",
        type = "tar.gz",
        sha256 = "7c5f0096a91d210159eceb2ff5e1c4da18388a170e1e3ce948aac9c8fdbbf595",
        strip_prefix = "enum-as-inner-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.enum-as-inner-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__env_logger__0_8_3",
        url = "https://crates.io/api/v1/crates/env_logger/0.8.3/download",
        type = "tar.gz",
        sha256 = "17392a012ea30ef05a610aa97dfb49496e71c9f676b27879922ea5bdf60d9d3f",
        strip_prefix = "env_logger-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.env_logger-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__erased_serde__0_3_13",
        url = "https://crates.io/api/v1/crates/erased-serde/0.3.13/download",
        type = "tar.gz",
        sha256 = "0465971a8cc1fa2455c8465aaa377131e1f1cf4983280f474a13e68793aa770c",
        strip_prefix = "erased-serde-0.3.13",
        build_file = Label("//rules/rust/remote:BUILD.erased-serde-0.3.13.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fail__0_4_0",
        url = "https://crates.io/api/v1/crates/fail/0.4.0/download",
        type = "tar.gz",
        sha256 = "3be3c61c59fdc91f5dbc3ea31ee8623122ce80057058be560654c5d410d181a6",
        strip_prefix = "fail-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.fail-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__failure__0_1_8",
        url = "https://crates.io/api/v1/crates/failure/0.1.8/download",
        type = "tar.gz",
        sha256 = "d32e9bd16cc02eae7db7ef620b392808b89f6a5e16bb3497d159c6b92a0f4f86",
        strip_prefix = "failure-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.failure-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__failure_derive__0_1_8",
        url = "https://crates.io/api/v1/crates/failure_derive/0.1.8/download",
        type = "tar.gz",
        sha256 = "aa4da3c766cd7a0db8242e326e9e4e081edd567072893ed320008189715366a4",
        strip_prefix = "failure_derive-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.failure_derive-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fallible_iterator__0_2_0",
        url = "https://crates.io/api/v1/crates/fallible-iterator/0.2.0/download",
        type = "tar.gz",
        sha256 = "4443176a9f2c162692bd3d352d745ef9413eec5782a80d8fd6f8a1ac692a07f7",
        strip_prefix = "fallible-iterator-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.fallible-iterator-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fancy_regex__0_3_5",
        url = "https://crates.io/api/v1/crates/fancy-regex/0.3.5/download",
        type = "tar.gz",
        sha256 = "ae91abf6555234338687bb47913978d275539235fcb77ba9863b779090b42b14",
        strip_prefix = "fancy-regex-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.fancy-regex-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fastdivide__0_3_0",
        url = "https://crates.io/api/v1/crates/fastdivide/0.3.0/download",
        type = "tar.gz",
        sha256 = "4a99a2d53cf90642500986ad22e5083b09e42d44c408f5f112e2a4a0925a643c",
        strip_prefix = "fastdivide-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.fastdivide-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__filetime__0_2_14",
        url = "https://crates.io/api/v1/crates/filetime/0.2.14/download",
        type = "tar.gz",
        sha256 = "1d34cfa13a63ae058bfa601fe9e313bbdb3746427c1459185464ce0fcf62e1e8",
        strip_prefix = "filetime-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.filetime-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__flate2__1_0_20",
        url = "https://crates.io/api/v1/crates/flate2/1.0.20/download",
        type = "tar.gz",
        sha256 = "cd3aec53de10fe96d7d8c565eb17f2c687bb5518a2ec453b5b1252964526abe0",
        strip_prefix = "flate2-1.0.20",
        build_file = Label("//rules/rust/remote:BUILD.flate2-1.0.20.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fnv__1_0_7",
        url = "https://crates.io/api/v1/crates/fnv/1.0.7/download",
        type = "tar.gz",
        sha256 = "3f9eec918d3f24069decb9af1554cad7c880e2da24a9afd88aca000531ab82c1",
        strip_prefix = "fnv-1.0.7",
        build_file = Label("//rules/rust/remote:BUILD.fnv-1.0.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__form_urlencoded__1_0_1",
        url = "https://crates.io/api/v1/crates/form_urlencoded/1.0.1/download",
        type = "tar.gz",
        sha256 = "5fc25a87fa4fd2094bffb06925852034d90a17f0d1e05197d4956d3555752191",
        strip_prefix = "form_urlencoded-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.form_urlencoded-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fs2__0_4_3",
        url = "https://crates.io/api/v1/crates/fs2/0.4.3/download",
        type = "tar.gz",
        sha256 = "9564fc758e15025b46aa6643b1b77d047d1a56a1aea6e01002ac0c7026876213",
        strip_prefix = "fs2-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.fs2-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fst__0_3_5",
        url = "https://crates.io/api/v1/crates/fst/0.3.5/download",
        type = "tar.gz",
        sha256 = "927fb434ff9f0115b215dc0efd2e4fbdd7448522a92a1aa37c77d6a2f8f1ebd6",
        strip_prefix = "fst-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.fst-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fst__0_4_5",
        url = "https://crates.io/api/v1/crates/fst/0.4.5/download",
        type = "tar.gz",
        sha256 = "d79238883cf0307100b90aba4a755d8051a3182305dfe7f649a1e9dc0517006f",
        strip_prefix = "fst-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.fst-0.4.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fuchsia_cprng__0_1_1",
        url = "https://crates.io/api/v1/crates/fuchsia-cprng/0.1.1/download",
        type = "tar.gz",
        sha256 = "a06f77d526c1a601b7c4cdd98f54b5eaabffc14d5f2f0296febdc7f357c6d3ba",
        strip_prefix = "fuchsia-cprng-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.fuchsia-cprng-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fuchsia_zircon__0_3_3",
        url = "https://crates.io/api/v1/crates/fuchsia-zircon/0.3.3/download",
        type = "tar.gz",
        sha256 = "2e9763c69ebaae630ba35f74888db465e49e259ba1bc0eda7d06f4a067615d82",
        strip_prefix = "fuchsia-zircon-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.fuchsia-zircon-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fuchsia_zircon_sys__0_3_3",
        url = "https://crates.io/api/v1/crates/fuchsia-zircon-sys/0.3.3/download",
        type = "tar.gz",
        sha256 = "3dcaa9ae7725d12cdb85b3ad99a434db70b468c09ded17e012d86b5c1010f7a7",
        strip_prefix = "fuchsia-zircon-sys-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.fuchsia-zircon-sys-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures__0_3_14",
        url = "https://crates.io/api/v1/crates/futures/0.3.14/download",
        type = "tar.gz",
        sha256 = "a9d5813545e459ad3ca1bff9915e9ad7f1a47dc6a91b627ce321d5863b7dd253",
        strip_prefix = "futures-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_channel__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-channel/0.3.14/download",
        type = "tar.gz",
        sha256 = "ce79c6a52a299137a6013061e0cf0e688fce5d7f1bc60125f520912fdb29ec25",
        strip_prefix = "futures-channel-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-channel-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_core__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-core/0.3.14/download",
        type = "tar.gz",
        sha256 = "098cd1c6dda6ca01650f1a37a794245eb73181d0d4d4e955e2f3c37db7af1815",
        strip_prefix = "futures-core-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-core-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_executor__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-executor/0.3.14/download",
        type = "tar.gz",
        sha256 = "10f6cb7042eda00f0049b1d2080aa4b93442997ee507eb3828e8bd7577f94c9d",
        strip_prefix = "futures-executor-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-executor-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_io__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-io/0.3.14/download",
        type = "tar.gz",
        sha256 = "365a1a1fb30ea1c03a830fdb2158f5236833ac81fa0ad12fe35b29cddc35cb04",
        strip_prefix = "futures-io-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-io-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_macro__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-macro/0.3.14/download",
        type = "tar.gz",
        sha256 = "668c6733a182cd7deb4f1de7ba3bf2120823835b3bcfbeacf7d2c4a773c1bb8b",
        strip_prefix = "futures-macro-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-macro-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_sink__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-sink/0.3.14/download",
        type = "tar.gz",
        sha256 = "5c5629433c555de3d82861a7a4e3794a4c40040390907cfbfd7143a92a426c23",
        strip_prefix = "futures-sink-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-sink-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_task__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-task/0.3.14/download",
        type = "tar.gz",
        sha256 = "ba7aa51095076f3ba6d9a1f702f74bd05ec65f555d70d2033d55ba8d69f581bc",
        strip_prefix = "futures-task-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-task-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_util__0_3_14",
        url = "https://crates.io/api/v1/crates/futures-util/0.3.14/download",
        type = "tar.gz",
        sha256 = "3c144ad54d60f23927f0a6b6d816e4271278b64f005ad65e4e35291d2de9c025",
        strip_prefix = "futures-util-0.3.14",
        build_file = Label("//rules/rust/remote:BUILD.futures-util-0.3.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fxhash__0_2_1",
        url = "https://crates.io/api/v1/crates/fxhash/0.2.1/download",
        type = "tar.gz",
        sha256 = "c31b6d751ae2c7f11320402d34e41349dd1016f8d5d45e48c4312bc8625af50c",
        strip_prefix = "fxhash-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.fxhash-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__generic_array__0_14_4",
        url = "https://crates.io/api/v1/crates/generic-array/0.14.4/download",
        type = "tar.gz",
        sha256 = "501466ecc8a30d1d3b7fc9229b122b2ce8ed6e9d9223f1138d4babb253e51817",
        strip_prefix = "generic-array-0.14.4",
        build_file = Label("//rules/rust/remote:BUILD.generic-array-0.14.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__getrandom__0_1_16",
        url = "https://crates.io/api/v1/crates/getrandom/0.1.16/download",
        type = "tar.gz",
        sha256 = "8fc3cb4d91f53b50155bdcfd23f6a4c39ae1969c2ae85982b135750cccaf5fce",
        strip_prefix = "getrandom-0.1.16",
        build_file = Label("//rules/rust/remote:BUILD.getrandom-0.1.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__getrandom__0_2_2",
        url = "https://crates.io/api/v1/crates/getrandom/0.2.2/download",
        type = "tar.gz",
        sha256 = "c9495705279e7140bf035dde1f6e750c162df8b625267cd52cc44e0b156732c8",
        strip_prefix = "getrandom-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.getrandom-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__gimli__0_23_0",
        url = "https://crates.io/api/v1/crates/gimli/0.23.0/download",
        type = "tar.gz",
        sha256 = "f6503fe142514ca4799d4c26297c4248239fe8838d827db6bd6065c6ed29a6ce",
        strip_prefix = "gimli-0.23.0",
        build_file = Label("//rules/rust/remote:BUILD.gimli-0.23.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__grpc__0_8_3",
        url = "https://crates.io/api/v1/crates/grpc/0.8.3/download",
        type = "tar.gz",
        sha256 = "efbd563cd51f8b9d3578a8029989b090aca83b8b411bfe1c7577b8b0f92937f8",
        strip_prefix = "grpc-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.grpc-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__grpc_compiler__0_8_3",
        url = "https://crates.io/api/v1/crates/grpc-compiler/0.8.3/download",
        type = "tar.gz",
        sha256 = "45f971449e16e799ebbf106d2414c115ff46f2849689c61da3a3271be0884a34",
        strip_prefix = "grpc-compiler-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.grpc-compiler-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__h2__0_2_7",
        url = "https://crates.io/api/v1/crates/h2/0.2.7/download",
        type = "tar.gz",
        sha256 = "5e4728fd124914ad25e99e3d15a9361a879f6620f63cb56bbb08f95abb97a535",
        strip_prefix = "h2-0.2.7",
        build_file = Label("//rules/rust/remote:BUILD.h2-0.2.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__half__1_7_1",
        url = "https://crates.io/api/v1/crates/half/1.7.1/download",
        type = "tar.gz",
        sha256 = "62aca2aba2d62b4a7f5b33f3712cb1b0692779a56fb510499d5c0aa594daeaf3",
        strip_prefix = "half-1.7.1",
        build_file = Label("//rules/rust/remote:BUILD.half-1.7.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hashbrown__0_9_1",
        url = "https://crates.io/api/v1/crates/hashbrown/0.9.1/download",
        type = "tar.gz",
        sha256 = "d7afe4a420e3fe79967a00898cc1f4db7c8a49a9333a29f8a4bd76a253d5cd04",
        strip_prefix = "hashbrown-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.hashbrown-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__heck__0_3_2",
        url = "https://crates.io/api/v1/crates/heck/0.3.2/download",
        type = "tar.gz",
        sha256 = "87cbf45460356b7deeb5e3415b5563308c0a9b057c85e12b06ad551f98d0a6ac",
        strip_prefix = "heck-0.3.2",
        build_file = Label("//rules/rust/remote:BUILD.heck-0.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hermit_abi__0_1_18",
        url = "https://crates.io/api/v1/crates/hermit-abi/0.1.18/download",
        type = "tar.gz",
        sha256 = "322f4de77956e22ed0e5032c359a0f1273f1f7f0d79bfa3b8ffbc730d7fbcc5c",
        strip_prefix = "hermit-abi-0.1.18",
        build_file = Label("//rules/rust/remote:BUILD.hermit-abi-0.1.18.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hmac__0_10_1",
        url = "https://crates.io/api/v1/crates/hmac/0.10.1/download",
        type = "tar.gz",
        sha256 = "c1441c6b1e930e2817404b5046f1f989899143a12bf92de603b69f4e0aee1e15",
        strip_prefix = "hmac-0.10.1",
        build_file = Label("//rules/rust/remote:BUILD.hmac-0.10.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hmac__0_9_0",
        url = "https://crates.io/api/v1/crates/hmac/0.9.0/download",
        type = "tar.gz",
        sha256 = "deae6d9dbb35ec2c502d62b8f7b1c000a0822c3b0794ba36b3149c0a1c840dff",
        strip_prefix = "hmac-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.hmac-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hostname__0_3_1",
        url = "https://crates.io/api/v1/crates/hostname/0.3.1/download",
        type = "tar.gz",
        sha256 = "3c731c3e10504cc8ed35cfe2f1db4c9274c3d35fa486e3b31df46f068ef3e867",
        strip_prefix = "hostname-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.hostname-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__htmlescape__0_3_1",
        url = "https://crates.io/api/v1/crates/htmlescape/0.3.1/download",
        type = "tar.gz",
        sha256 = "e9025058dae765dee5070ec375f591e2ba14638c63feff74f13805a72e523163",
        strip_prefix = "htmlescape-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.htmlescape-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__http__0_2_4",
        url = "https://crates.io/api/v1/crates/http/0.2.4/download",
        type = "tar.gz",
        sha256 = "527e8c9ac747e28542699a951517aa9a6945af506cd1f2e1b53a576c17b6cc11",
        strip_prefix = "http-0.2.4",
        build_file = Label("//rules/rust/remote:BUILD.http-0.2.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__httparse__1_4_0",
        url = "https://crates.io/api/v1/crates/httparse/1.4.0/download",
        type = "tar.gz",
        sha256 = "4a1ce40d6fc9764887c2fdc7305c3dcc429ba11ff981c1509416afd5697e4437",
        strip_prefix = "httparse-1.4.0",
        build_file = Label("//rules/rust/remote:BUILD.httparse-1.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__httpbis__0_9_1",
        url = "https://crates.io/api/v1/crates/httpbis/0.9.1/download",
        type = "tar.gz",
        sha256 = "3d3e4404f8f87938a2db89336609bde64363f5a556b15af936343e7252c9648d",
        strip_prefix = "httpbis-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.httpbis-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__humantime__1_3_0",
        url = "https://crates.io/api/v1/crates/humantime/1.3.0/download",
        type = "tar.gz",
        sha256 = "df004cfca50ef23c36850aaaa59ad52cc70d0e90243c3c7737a4dd32dc7a3c4f",
        strip_prefix = "humantime-1.3.0",
        build_file = Label("//rules/rust/remote:BUILD.humantime-1.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__humantime__2_1_0",
        url = "https://crates.io/api/v1/crates/humantime/2.1.0/download",
        type = "tar.gz",
        sha256 = "9a3a5bfb195931eeb336b2a7b4d761daec841b97f947d34394601737a7bba5e4",
        strip_prefix = "humantime-2.1.0",
        build_file = Label("//rules/rust/remote:BUILD.humantime-2.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__idna__0_2_3",
        url = "https://crates.io/api/v1/crates/idna/0.2.3/download",
        type = "tar.gz",
        sha256 = "418a0a6fab821475f634efe3ccc45c013f742efe03d853e8d3355d5cb850ecf8",
        strip_prefix = "idna-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.idna-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__indexmap__1_6_2",
        url = "https://crates.io/api/v1/crates/indexmap/1.6.2/download",
        type = "tar.gz",
        sha256 = "824845a0bf897a9042383849b02c1bc219c2383772efcd5c6f9766fa4b81aef3",
        strip_prefix = "indexmap-1.6.2",
        build_file = Label("//rules/rust/remote:BUILD.indexmap-1.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__instant__0_1_9",
        url = "https://crates.io/api/v1/crates/instant/0.1.9/download",
        type = "tar.gz",
        sha256 = "61124eeebbd69b8190558df225adf7e4caafce0d743919e5d6b19652314ec5ec",
        strip_prefix = "instant-0.1.9",
        build_file = Label("//rules/rust/remote:BUILD.instant-0.1.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__integer_encoding__2_1_3",
        url = "https://crates.io/api/v1/crates/integer-encoding/2.1.3/download",
        type = "tar.gz",
        sha256 = "c27df786dcc3a75ccd134f83ece166af0a1e5785d52b12b7375d0d063e1d5c47",
        strip_prefix = "integer-encoding-2.1.3",
        build_file = Label("//rules/rust/remote:BUILD.integer-encoding-2.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__iovec__0_1_4",
        url = "https://crates.io/api/v1/crates/iovec/0.1.4/download",
        type = "tar.gz",
        sha256 = "b2b3ea6ff95e175473f8ffe6a7eb7c00d054240321b84c57051175fe3c1e075e",
        strip_prefix = "iovec-0.1.4",
        build_file = Label("//rules/rust/remote:BUILD.iovec-0.1.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ipconfig__0_2_2",
        url = "https://crates.io/api/v1/crates/ipconfig/0.2.2/download",
        type = "tar.gz",
        sha256 = "f7e2f18aece9709094573a9f24f483c4f65caa4298e2f7ae1b71cc65d853fad7",
        strip_prefix = "ipconfig-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.ipconfig-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itertools__0_10_0",
        url = "https://crates.io/api/v1/crates/itertools/0.10.0/download",
        type = "tar.gz",
        sha256 = "37d572918e350e82412fe766d24b15e6682fb2ed2bbe018280caa810397cb319",
        strip_prefix = "itertools-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.itertools-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itertools__0_9_0",
        url = "https://crates.io/api/v1/crates/itertools/0.9.0/download",
        type = "tar.gz",
        sha256 = "284f18f85651fe11e8a991b2adb42cb078325c996ed026d994719efcfca1d54b",
        strip_prefix = "itertools-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.itertools-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itoa__0_4_7",
        url = "https://crates.io/api/v1/crates/itoa/0.4.7/download",
        type = "tar.gz",
        sha256 = "dd25036021b0de88a0aff6b850051563c6516d0bf53f8638938edbb9de732736",
        strip_prefix = "itoa-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.itoa-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__js_sys__0_3_50",
        url = "https://crates.io/api/v1/crates/js-sys/0.3.50/download",
        type = "tar.gz",
        sha256 = "2d99f9e3e84b8f67f846ef5b4cbbc3b1c29f6c759fcbce6f01aa0e73d932a24c",
        strip_prefix = "js-sys-0.3.50",
        build_file = Label("//rules/rust/remote:BUILD.js-sys-0.3.50.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__kernel32_sys__0_2_2",
        url = "https://crates.io/api/v1/crates/kernel32-sys/0.2.2/download",
        type = "tar.gz",
        sha256 = "7507624b29483431c0ba2d82aece8ca6cdba9382bff4ddd0f7490560c056098d",
        strip_prefix = "kernel32-sys-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.kernel32-sys-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__language_tags__0_2_2",
        url = "https://crates.io/api/v1/crates/language-tags/0.2.2/download",
        type = "tar.gz",
        sha256 = "a91d884b6667cd606bb5a69aa0c99ba811a115fc68915e7056ec08a46e93199a",
        strip_prefix = "language-tags-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.language-tags-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lazy_static__1_4_0",
        url = "https://crates.io/api/v1/crates/lazy_static/1.4.0/download",
        type = "tar.gz",
        sha256 = "e2abad23fbc42b3700f2f279844dc832adb2b2eb069b2df918f455c4e18cc646",
        strip_prefix = "lazy_static-1.4.0",
        build_file = Label("//rules/rust/remote:BUILD.lazy_static-1.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__levenshtein_automata__0_1_1",
        url = "https://crates.io/api/v1/crates/levenshtein_automata/0.1.1/download",
        type = "tar.gz",
        sha256 = "73a004f877f468548d8d0ac4977456a249d8fabbdb8416c36db163dfc8f2e8ca",
        strip_prefix = "levenshtein_automata-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.levenshtein_automata-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lexical_core__0_7_5",
        url = "https://crates.io/api/v1/crates/lexical-core/0.7.5/download",
        type = "tar.gz",
        sha256 = "21f866863575d0e1d654fbeeabdc927292fdf862873dc3c96c6f753357e13374",
        strip_prefix = "lexical-core-0.7.5",
        build_file = Label("//rules/rust/remote:BUILD.lexical-core-0.7.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__libc__0_2_93",
        url = "https://crates.io/api/v1/crates/libc/0.2.93/download",
        type = "tar.gz",
        sha256 = "9385f66bf6105b241aa65a61cb923ef20efc665cb9f9bb50ac2f0c4b7f378d41",
        strip_prefix = "libc-0.2.93",
        build_file = Label("//rules/rust/remote:BUILD.libc-0.2.93.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__linked_hash_map__0_5_4",
        url = "https://crates.io/api/v1/crates/linked-hash-map/0.5.4/download",
        type = "tar.gz",
        sha256 = "7fb9b38af92608140b86b693604b9ffcc5824240a484d1ecd4795bacb2fe88f3",
        strip_prefix = "linked-hash-map-0.5.4",
        build_file = Label("//rules/rust/remote:BUILD.linked-hash-map-0.5.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lock_api__0_4_3",
        url = "https://crates.io/api/v1/crates/lock_api/0.4.3/download",
        type = "tar.gz",
        sha256 = "5a3c91c24eae6777794bb1997ad98bbb87daf92890acab859f7eaa4320333176",
        strip_prefix = "lock_api-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.lock_api-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log__0_4_14",
        url = "https://crates.io/api/v1/crates/log/0.4.14/download",
        type = "tar.gz",
        sha256 = "51b9bbe6c47d51fc3e1a9b945965946b4c44142ab8792c50835a980d362c2710",
        strip_prefix = "log-0.4.14",
        build_file = Label("//rules/rust/remote:BUILD.log-0.4.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log_mdc__0_1_0",
        url = "https://crates.io/api/v1/crates/log-mdc/0.1.0/download",
        type = "tar.gz",
        sha256 = "a94d21414c1f4a51209ad204c1776a3d0765002c76c6abcb602a6f09f1e881c7",
        strip_prefix = "log-mdc-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.log-mdc-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log_ndc__0_2_0",
        url = "https://crates.io/api/v1/crates/log-ndc/0.2.0/download",
        type = "tar.gz",
        sha256 = "edb09057c7b58b7d27498b528eaee9a1e661b2974a733fcabbbc3350360bc8bd",
        strip_prefix = "log-ndc-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.log-ndc-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log4rs__0_10_0",
        url = "https://crates.io/api/v1/crates/log4rs/0.10.0/download",
        type = "tar.gz",
        sha256 = "853db99624c59798ddcf027dbe486541dd5cb5008ac6a6aaf217cc6fa044ee71",
        strip_prefix = "log4rs-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.log4rs-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lru__0_6_5",
        url = "https://crates.io/api/v1/crates/lru/0.6.5/download",
        type = "tar.gz",
        sha256 = "1f374d42cdfc1d7dbf3d3dec28afab2eb97ffbf43a3234d795b5986dbf4b90ba",
        strip_prefix = "lru-0.6.5",
        build_file = Label("//rules/rust/remote:BUILD.lru-0.6.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lru_cache__0_1_2",
        url = "https://crates.io/api/v1/crates/lru-cache/0.1.2/download",
        type = "tar.gz",
        sha256 = "31e24f1ad8321ca0e8a1e0ac13f23cb668e6f5466c2c57319f6a5cf1cc8e3b1c",
        strip_prefix = "lru-cache-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.lru-cache-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lz4__1_23_2",
        url = "https://crates.io/api/v1/crates/lz4/1.23.2/download",
        type = "tar.gz",
        sha256 = "aac20ed6991e01bf6a2e68cc73df2b389707403662a8ba89f68511fb340f724c",
        strip_prefix = "lz4-1.23.2",
        build_file = Label("//rules/rust/remote:BUILD.lz4-1.23.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lz4_sys__1_9_2",
        url = "https://crates.io/api/v1/crates/lz4-sys/1.9.2/download",
        type = "tar.gz",
        sha256 = "dca79aa95d8b3226213ad454d328369853be3a1382d89532a854f4d69640acae",
        strip_prefix = "lz4-sys-1.9.2",
        build_file = Label("//rules/rust/remote:BUILD.lz4-sys-1.9.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__maplit__1_0_2",
        url = "https://crates.io/api/v1/crates/maplit/1.0.2/download",
        type = "tar.gz",
        sha256 = "3e2e65a1a2e43cfcb47a895c4c8b10d1f4a61097f9f254f183aee60cad9c651d",
        strip_prefix = "maplit-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.maplit-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__match_cfg__0_1_0",
        url = "https://crates.io/api/v1/crates/match_cfg/0.1.0/download",
        type = "tar.gz",
        sha256 = "ffbee8634e0d45d258acb448e7eaab3fce7a0a467395d4d9f228e3c1f01fb2e4",
        strip_prefix = "match_cfg-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.match_cfg-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__matches__0_1_8",
        url = "https://crates.io/api/v1/crates/matches/0.1.8/download",
        type = "tar.gz",
        sha256 = "7ffc5c5338469d4d3ea17d269fa8ea3512ad247247c30bd2df69e68309ed0a08",
        strip_prefix = "matches-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.matches-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__maybe_uninit__2_0_0",
        url = "https://crates.io/api/v1/crates/maybe-uninit/2.0.0/download",
        type = "tar.gz",
        sha256 = "60302e4db3a61da70c0cb7991976248362f30319e88850c487b9b95bbf059e00",
        strip_prefix = "maybe-uninit-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.maybe-uninit-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__md_5__0_9_1",
        url = "https://crates.io/api/v1/crates/md-5/0.9.1/download",
        type = "tar.gz",
        sha256 = "7b5a279bb9607f9f53c22d496eade00d138d1bdcccd07d74650387cf94942a15",
        strip_prefix = "md-5-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.md-5-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__md5__0_7_0",
        url = "https://crates.io/api/v1/crates/md5/0.7.0/download",
        type = "tar.gz",
        sha256 = "490cc448043f947bae3cbee9c203358d62dbee0db12107a74be5c30ccfd09771",
        strip_prefix = "md5-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.md5-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memchr__2_3_4",
        url = "https://crates.io/api/v1/crates/memchr/2.3.4/download",
        type = "tar.gz",
        sha256 = "0ee1c47aaa256ecabcaea351eae4a9b01ef39ed810004e298d2511ed284b1525",
        strip_prefix = "memchr-2.3.4",
        build_file = Label("//rules/rust/remote:BUILD.memchr-2.3.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memmap__0_7_0",
        url = "https://crates.io/api/v1/crates/memmap/0.7.0/download",
        type = "tar.gz",
        sha256 = "6585fd95e7bb50d6cc31e20d4cf9afb4e2ba16c5846fc76793f11218da9c475b",
        strip_prefix = "memmap-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.memmap-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memoffset__0_5_6",
        url = "https://crates.io/api/v1/crates/memoffset/0.5.6/download",
        type = "tar.gz",
        sha256 = "043175f069eda7b85febe4a74abbaeff828d9f8b448515d3151a14a3542811aa",
        strip_prefix = "memoffset-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.memoffset-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memoffset__0_6_3",
        url = "https://crates.io/api/v1/crates/memoffset/0.6.3/download",
        type = "tar.gz",
        sha256 = "f83fb6581e8ed1f85fd45c116db8405483899489e38406156c25eb743554361d",
        strip_prefix = "memoffset-0.6.3",
        build_file = Label("//rules/rust/remote:BUILD.memoffset-0.6.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mime__0_3_16",
        url = "https://crates.io/api/v1/crates/mime/0.3.16/download",
        type = "tar.gz",
        sha256 = "2a60c7ce501c71e03a9c9c0d35b861413ae925bd979cc7a4e30d060069aaac8d",
        strip_prefix = "mime-0.3.16",
        build_file = Label("//rules/rust/remote:BUILD.mime-0.3.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miniz_oxide__0_4_4",
        url = "https://crates.io/api/v1/crates/miniz_oxide/0.4.4/download",
        type = "tar.gz",
        sha256 = "a92518e98c078586bc6c934028adcca4c92a53d6a958196de835170a01d84e4b",
        strip_prefix = "miniz_oxide-0.4.4",
        build_file = Label("//rules/rust/remote:BUILD.miniz_oxide-0.4.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio__0_6_23",
        url = "https://crates.io/api/v1/crates/mio/0.6.23/download",
        type = "tar.gz",
        sha256 = "4afd66f5b91bf2a3bc13fad0e21caedac168ca4c707504e75585648ae80e4cc4",
        strip_prefix = "mio-0.6.23",
        build_file = Label("//rules/rust/remote:BUILD.mio-0.6.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio__0_7_11",
        url = "https://crates.io/api/v1/crates/mio/0.7.11/download",
        type = "tar.gz",
        sha256 = "cf80d3e903b34e0bd7282b218398aec54e082c840d9baf8339e0080a0c542956",
        strip_prefix = "mio-0.7.11",
        build_file = Label("//rules/rust/remote:BUILD.mio-0.7.11.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio_named_pipes__0_1_7",
        url = "https://crates.io/api/v1/crates/mio-named-pipes/0.1.7/download",
        type = "tar.gz",
        sha256 = "0840c1c50fd55e521b247f949c241c9997709f23bd7f023b9762cd561e935656",
        strip_prefix = "mio-named-pipes-0.1.7",
        build_file = Label("//rules/rust/remote:BUILD.mio-named-pipes-0.1.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio_uds__0_6_8",
        url = "https://crates.io/api/v1/crates/mio-uds/0.6.8/download",
        type = "tar.gz",
        sha256 = "afcb699eb26d4332647cc848492bbc15eafb26f08d0304550d5aa1f612e066f0",
        strip_prefix = "mio-uds-0.6.8",
        build_file = Label("//rules/rust/remote:BUILD.mio-uds-0.6.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miow__0_2_2",
        url = "https://crates.io/api/v1/crates/miow/0.2.2/download",
        type = "tar.gz",
        sha256 = "ebd808424166322d4a38da87083bfddd3ac4c131334ed55856112eb06d46944d",
        strip_prefix = "miow-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.miow-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miow__0_3_7",
        url = "https://crates.io/api/v1/crates/miow/0.3.7/download",
        type = "tar.gz",
        sha256 = "b9f1c5b025cda876f66ef43a113f91ebc9f4ccef34843000e0adf6ebbab84e21",
        strip_prefix = "miow-0.3.7",
        build_file = Label("//rules/rust/remote:BUILD.miow-0.3.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__murmurhash32__0_2_0",
        url = "https://crates.io/api/v1/crates/murmurhash32/0.2.0/download",
        type = "tar.gz",
        sha256 = "d736ff882f0e85fe9689fb23db229616c4c00aee2b3ac282f666d8f20eb25d4a",
        strip_prefix = "murmurhash32-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.murmurhash32-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__net2__0_2_37",
        url = "https://crates.io/api/v1/crates/net2/0.2.37/download",
        type = "tar.gz",
        sha256 = "391630d12b68002ae1e25e8f974306474966550ad82dac6886fb8910c19568ae",
        strip_prefix = "net2-0.2.37",
        build_file = Label("//rules/rust/remote:BUILD.net2-0.2.37.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__nix__0_14_1",
        url = "https://crates.io/api/v1/crates/nix/0.14.1/download",
        type = "tar.gz",
        sha256 = "6c722bee1037d430d0f8e687bbdbf222f27cc6e4e68d5caf630857bb2b6dbdce",
        strip_prefix = "nix-0.14.1",
        build_file = Label("//rules/rust/remote:BUILD.nix-0.14.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__nom__5_1_2",
        url = "https://crates.io/api/v1/crates/nom/5.1.2/download",
        type = "tar.gz",
        sha256 = "ffb4262d26ed83a1c0a33a38fe2bb15797329c85770da05e6b828ddb782627af",
        strip_prefix = "nom-5.1.2",
        build_file = Label("//rules/rust/remote:BUILD.nom-5.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ntapi__0_3_6",
        url = "https://crates.io/api/v1/crates/ntapi/0.3.6/download",
        type = "tar.gz",
        sha256 = "3f6bb902e437b6d86e03cce10a7e2af662292c5dfef23b65899ea3ac9354ad44",
        strip_prefix = "ntapi-0.3.6",
        build_file = Label("//rules/rust/remote:BUILD.ntapi-0.3.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_bigint__0_3_2",
        url = "https://crates.io/api/v1/crates/num-bigint/0.3.2/download",
        type = "tar.gz",
        sha256 = "7d0a3d5e207573f948a9e5376662aa743a2ea13f7c50a554d7af443a73fbfeba",
        strip_prefix = "num-bigint-0.3.2",
        build_file = Label("//rules/rust/remote:BUILD.num-bigint-0.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_integer__0_1_44",
        url = "https://crates.io/api/v1/crates/num-integer/0.1.44/download",
        type = "tar.gz",
        sha256 = "d2cc698a63b549a70bc047073d2949cce27cd1c7b0a4a862d08a8031bc2801db",
        strip_prefix = "num-integer-0.1.44",
        build_file = Label("//rules/rust/remote:BUILD.num-integer-0.1.44.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_traits__0_1_43",
        url = "https://crates.io/api/v1/crates/num-traits/0.1.43/download",
        type = "tar.gz",
        sha256 = "92e5113e9fd4cc14ded8e499429f396a20f98c772a47cc8622a736e1ec843c31",
        strip_prefix = "num-traits-0.1.43",
        build_file = Label("//rules/rust/remote:BUILD.num-traits-0.1.43.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_traits__0_2_14",
        url = "https://crates.io/api/v1/crates/num-traits/0.2.14/download",
        type = "tar.gz",
        sha256 = "9a64b1ec5cda2586e284722486d802acf1f7dbdc623e2bfc57e65ca1cd099290",
        strip_prefix = "num-traits-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.num-traits-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_cpus__1_13_0",
        url = "https://crates.io/api/v1/crates/num_cpus/1.13.0/download",
        type = "tar.gz",
        sha256 = "05499f3756671c15885fee9034446956fff3f243d6077b91e5767df161f766b3",
        strip_prefix = "num_cpus-1.13.0",
        build_file = Label("//rules/rust/remote:BUILD.num_cpus-1.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__object__0_23_0",
        url = "https://crates.io/api/v1/crates/object/0.23.0/download",
        type = "tar.gz",
        sha256 = "a9a7ab5d64814df0fe4a4b5ead45ed6c5f181ee3ff04ba344313a6c80446c5d4",
        strip_prefix = "object-0.23.0",
        build_file = Label("//rules/rust/remote:BUILD.object-0.23.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__once_cell__1_7_2",
        url = "https://crates.io/api/v1/crates/once_cell/1.7.2/download",
        type = "tar.gz",
        sha256 = "af8b08b04175473088b46763e51ee54da5f9a164bc162f615b91bc179dbf15a3",
        strip_prefix = "once_cell-1.7.2",
        build_file = Label("//rules/rust/remote:BUILD.once_cell-1.7.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__oorandom__11_1_3",
        url = "https://crates.io/api/v1/crates/oorandom/11.1.3/download",
        type = "tar.gz",
        sha256 = "0ab1bc2a289d34bd04a330323ac98a1b4bc82c9d9fcb1e66b63caa84da26b575",
        strip_prefix = "oorandom-11.1.3",
        build_file = Label("//rules/rust/remote:BUILD.oorandom-11.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__opaque_debug__0_3_0",
        url = "https://crates.io/api/v1/crates/opaque-debug/0.3.0/download",
        type = "tar.gz",
        sha256 = "624a8340c38c1b80fd549087862da4ba43e08858af025b236e509b6649fc13d5",
        strip_prefix = "opaque-debug-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.opaque-debug-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ordered_float__1_1_1",
        url = "https://crates.io/api/v1/crates/ordered-float/1.1.1/download",
        type = "tar.gz",
        sha256 = "3305af35278dd29f46fcdd139e0b1fbfae2153f0e5928b39b035542dd31e37b7",
        strip_prefix = "ordered-float-1.1.1",
        build_file = Label("//rules/rust/remote:BUILD.ordered-float-1.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__owned_read__0_4_1",
        url = "https://crates.io/api/v1/crates/owned-read/0.4.1/download",
        type = "tar.gz",
        sha256 = "b66d1e235abcebc845cf93550b89b74f468c051496fafb433ede4104b9f71ba1",
        strip_prefix = "owned-read-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.owned-read-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__owning_ref__0_4_1",
        url = "https://crates.io/api/v1/crates/owning_ref/0.4.1/download",
        type = "tar.gz",
        sha256 = "6ff55baddef9e4ad00f88b6c743a2a8062d4c6ade126c2a528644b8e444d52ce",
        strip_prefix = "owning_ref-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.owning_ref-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot__0_11_1",
        url = "https://crates.io/api/v1/crates/parking_lot/0.11.1/download",
        type = "tar.gz",
        sha256 = "6d7744ac029df22dca6284efe4e898991d28e3085c706c972bcd7da4a27a15eb",
        strip_prefix = "parking_lot-0.11.1",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot-0.11.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot_core__0_8_3",
        url = "https://crates.io/api/v1/crates/parking_lot_core/0.8.3/download",
        type = "tar.gz",
        sha256 = "fa7a782938e745763fe6907fc6ba86946d72f49fe7e21de074e08128a99fb018",
        strip_prefix = "parking_lot_core-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot_core-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__percent_encoding__2_1_0",
        url = "https://crates.io/api/v1/crates/percent-encoding/2.1.0/download",
        type = "tar.gz",
        sha256 = "d4fd5641d01c8f18a23da7b6fe29298ff4b55afcccdf78973b24cf3175fee32e",
        strip_prefix = "percent-encoding-2.1.0",
        build_file = Label("//rules/rust/remote:BUILD.percent-encoding-2.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__phf__0_8_0",
        url = "https://crates.io/api/v1/crates/phf/0.8.0/download",
        type = "tar.gz",
        sha256 = "3dfb61232e34fcb633f43d12c58f83c1df82962dcdfa565a4e866ffc17dafe12",
        strip_prefix = "phf-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.phf-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__phf_shared__0_8_0",
        url = "https://crates.io/api/v1/crates/phf_shared/0.8.0/download",
        type = "tar.gz",
        sha256 = "c00cf8b9eafe68dde5e9eaa2cef8ee84a9336a47d566ec55ca16589633b65af7",
        strip_prefix = "phf_shared-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.phf_shared-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project__0_4_28",
        url = "https://crates.io/api/v1/crates/pin-project/0.4.28/download",
        type = "tar.gz",
        sha256 = "918192b5c59119d51e0cd221f4d49dde9112824ba717369e903c97d076083d0f",
        strip_prefix = "pin-project-0.4.28",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-0.4.28.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project__1_0_7",
        url = "https://crates.io/api/v1/crates/pin-project/1.0.7/download",
        type = "tar.gz",
        sha256 = "c7509cc106041c40a4518d2af7a61530e1eed0e6285296a3d8c5472806ccc4a4",
        strip_prefix = "pin-project-1.0.7",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-1.0.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_internal__0_4_28",
        url = "https://crates.io/api/v1/crates/pin-project-internal/0.4.28/download",
        type = "tar.gz",
        sha256 = "3be26700300be6d9d23264c73211d8190e755b6b5ca7a1b28230025511b52a5e",
        strip_prefix = "pin-project-internal-0.4.28",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-internal-0.4.28.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_internal__1_0_7",
        url = "https://crates.io/api/v1/crates/pin-project-internal/1.0.7/download",
        type = "tar.gz",
        sha256 = "48c950132583b500556b1efd71d45b319029f2b71518d979fcc208e16b42426f",
        strip_prefix = "pin-project-internal-1.0.7",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-internal-1.0.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_lite__0_1_12",
        url = "https://crates.io/api/v1/crates/pin-project-lite/0.1.12/download",
        type = "tar.gz",
        sha256 = "257b64915a082f7811703966789728173279bdebb956b143dbcd23f6f970a777",
        strip_prefix = "pin-project-lite-0.1.12",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-lite-0.1.12.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_lite__0_2_6",
        url = "https://crates.io/api/v1/crates/pin-project-lite/0.2.6/download",
        type = "tar.gz",
        sha256 = "dc0e1f259c92177c30a4c9d177246edd0a3568b25756a977d0632cf8fa37e905",
        strip_prefix = "pin-project-lite-0.2.6",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-lite-0.2.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_utils__0_1_0",
        url = "https://crates.io/api/v1/crates/pin-utils/0.1.0/download",
        type = "tar.gz",
        sha256 = "8b870d8c151b6f2fb93e84a13146138f05d02ed11c7e7c54f8826aaaf7c9f184",
        strip_prefix = "pin-utils-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.pin-utils-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__plotters__0_3_0",
        url = "https://crates.io/api/v1/crates/plotters/0.3.0/download",
        type = "tar.gz",
        sha256 = "45ca0ae5f169d0917a7c7f5a9c1a3d3d9598f18f529dd2b8373ed988efea307a",
        strip_prefix = "plotters-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.plotters-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__plotters_backend__0_3_0",
        url = "https://crates.io/api/v1/crates/plotters-backend/0.3.0/download",
        type = "tar.gz",
        sha256 = "b07fffcddc1cb3a1de753caa4e4df03b79922ba43cf882acc1bdd7e8df9f4590",
        strip_prefix = "plotters-backend-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.plotters-backend-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__plotters_svg__0_3_0",
        url = "https://crates.io/api/v1/crates/plotters-svg/0.3.0/download",
        type = "tar.gz",
        sha256 = "b38a02e23bd9604b842a812063aec4ef702b57989c37b655254bb61c471ad211",
        strip_prefix = "plotters-svg-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.plotters-svg-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres__0_17_5",
        url = "https://crates.io/api/v1/crates/postgres/0.17.5/download",
        type = "tar.gz",
        sha256 = "14d864cf6c2eabf1323afe4145ff273aad1898e4f2a3bcb30347715df8624a07",
        strip_prefix = "postgres-0.17.5",
        build_file = Label("//rules/rust/remote:BUILD.postgres-0.17.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_derive__0_4_0",
        url = "https://crates.io/api/v1/crates/postgres-derive/0.4.0/download",
        type = "tar.gz",
        sha256 = "c857dd221cb0e7d8414b894a0ce29eae44d453dda0baa132447878e75e701477",
        strip_prefix = "postgres-derive-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.postgres-derive-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_protocol__0_5_3",
        url = "https://crates.io/api/v1/crates/postgres-protocol/0.5.3/download",
        type = "tar.gz",
        sha256 = "4888a0e36637ab38d76cace88c1476937d617ad015f07f6b669cec11beacc019",
        strip_prefix = "postgres-protocol-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.postgres-protocol-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_protocol__0_6_1",
        url = "https://crates.io/api/v1/crates/postgres-protocol/0.6.1/download",
        type = "tar.gz",
        sha256 = "ff3e0f70d32e20923cabf2df02913be7c1842d4c772db8065c00fcfdd1d1bff3",
        strip_prefix = "postgres-protocol-0.6.1",
        build_file = Label("//rules/rust/remote:BUILD.postgres-protocol-0.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_types__0_1_3",
        url = "https://crates.io/api/v1/crates/postgres-types/0.1.3/download",
        type = "tar.gz",
        sha256 = "cfc08a7d94a80665de4a83942fa8db2fdeaf2f123fc0535e384dc4fff251efae",
        strip_prefix = "postgres-types-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.postgres-types-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__postgres_types__0_2_1",
        url = "https://crates.io/api/v1/crates/postgres-types/0.2.1/download",
        type = "tar.gz",
        sha256 = "430f4131e1b7657b0cd9a2b0c3408d77c9a43a042d300b8c77f981dffcc43a2f",
        strip_prefix = "postgres-types-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.postgres-types-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ppv_lite86__0_2_10",
        url = "https://crates.io/api/v1/crates/ppv-lite86/0.2.10/download",
        type = "tar.gz",
        sha256 = "ac74c624d6b2d21f425f752262f42188365d7b8ff1aff74c82e45136510a4857",
        strip_prefix = "ppv-lite86-0.2.10",
        build_file = Label("//rules/rust/remote:BUILD.ppv-lite86-0.2.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro_hack__0_5_19",
        url = "https://crates.io/api/v1/crates/proc-macro-hack/0.5.19/download",
        type = "tar.gz",
        sha256 = "dbf0c48bc1d91375ae5c3cd81e3722dff1abcf81a30960240640d223f59fe0e5",
        strip_prefix = "proc-macro-hack-0.5.19",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro-hack-0.5.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro_nested__0_1_7",
        url = "https://crates.io/api/v1/crates/proc-macro-nested/0.1.7/download",
        type = "tar.gz",
        sha256 = "bc881b2c22681370c6a780e47af9840ef841837bc98118431d4e1868bd0c1086",
        strip_prefix = "proc-macro-nested-0.1.7",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro-nested-0.1.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro2__1_0_26",
        url = "https://crates.io/api/v1/crates/proc-macro2/1.0.26/download",
        type = "tar.gz",
        sha256 = "a152013215dca273577e18d2bf00fa862b89b24169fb78c4c95aeb07992c9cec",
        strip_prefix = "proc-macro2-1.0.26",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro2-1.0.26.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proptest__0_10_1",
        url = "https://crates.io/api/v1/crates/proptest/0.10.1/download",
        type = "tar.gz",
        sha256 = "12e6c80c1139113c28ee4670dc50cc42915228b51f56a9e407f0ec60f966646f",
        strip_prefix = "proptest-0.10.1",
        build_file = Label("//rules/rust/remote:BUILD.proptest-0.10.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__protobuf__2_18_2",
        url = "https://crates.io/api/v1/crates/protobuf/2.18.2/download",
        type = "tar.gz",
        sha256 = "fe8e18df92889779cfe50ccf640173141ff73c5b2817e553d6d35230f798a036",
        strip_prefix = "protobuf-2.18.2",
        build_file = Label("//rules/rust/remote:BUILD.protobuf-2.18.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__protobuf_codegen__2_18_2",
        url = "https://crates.io/api/v1/crates/protobuf-codegen/2.18.2/download",
        type = "tar.gz",
        sha256 = "f49782fe28b5ff7d5d51cbfbe8985f3ff863acea663c515ed369c53f72e1d628",
        strip_prefix = "protobuf-codegen-2.18.2",
        build_file = Label("//rules/rust/remote:BUILD.protobuf-codegen-2.18.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__quick_error__1_2_3",
        url = "https://crates.io/api/v1/crates/quick-error/1.2.3/download",
        type = "tar.gz",
        sha256 = "a1d01941d82fa2ab50be1e79e6714289dd7cde78eba4c074bc5a4374f650dfe0",
        strip_prefix = "quick-error-1.2.3",
        build_file = Label("//rules/rust/remote:BUILD.quick-error-1.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__quote__1_0_9",
        url = "https://crates.io/api/v1/crates/quote/1.0.9/download",
        type = "tar.gz",
        sha256 = "c3d0b9745dc2debf507c8422de05d7226cc1f0644216dfdfead988f9b1ab32a7",
        strip_prefix = "quote-1.0.9",
        build_file = Label("//rules/rust/remote:BUILD.quote-1.0.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__r2d2__0_8_9",
        url = "https://crates.io/api/v1/crates/r2d2/0.8.9/download",
        type = "tar.gz",
        sha256 = "545c5bc2b880973c9c10e4067418407a0ccaa3091781d1671d46eb35107cb26f",
        strip_prefix = "r2d2-0.8.9",
        build_file = Label("//rules/rust/remote:BUILD.r2d2-0.8.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__r2d2_postgres__0_16_0",
        url = "https://crates.io/api/v1/crates/r2d2_postgres/0.16.0/download",
        type = "tar.gz",
        sha256 = "707d27f66f43bac1081141f6d9611fffcce7da2841ae97c7ac53619d098efe8f",
        strip_prefix = "r2d2_postgres-0.16.0",
        build_file = Label("//rules/rust/remote:BUILD.r2d2_postgres-0.16.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_4_6",
        url = "https://crates.io/api/v1/crates/rand/0.4.6/download",
        type = "tar.gz",
        sha256 = "552840b97013b1a26992c11eac34bdd778e464601a4c2054b5f0bff7c6761293",
        strip_prefix = "rand-0.4.6",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.4.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_5_6",
        url = "https://crates.io/api/v1/crates/rand/0.5.6/download",
        type = "tar.gz",
        sha256 = "c618c47cd3ebd209790115ab837de41425723956ad3ce2e6a7f09890947cacb9",
        strip_prefix = "rand-0.5.6",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.5.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_7_3",
        url = "https://crates.io/api/v1/crates/rand/0.7.3/download",
        type = "tar.gz",
        sha256 = "6a6b1679d49b24bbfe0c803429aa1874472f50d9b363131f0e89fc356b544d03",
        strip_prefix = "rand-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_8_3",
        url = "https://crates.io/api/v1/crates/rand/0.8.3/download",
        type = "tar.gz",
        sha256 = "0ef9e7e66b4468674bfcb0c81af8b7fa0bb154fa9f28eb840da5c447baeb8d7e",
        strip_prefix = "rand-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_chacha__0_2_2",
        url = "https://crates.io/api/v1/crates/rand_chacha/0.2.2/download",
        type = "tar.gz",
        sha256 = "f4c8ed856279c9737206bf725bf36935d8666ead7aa69b52be55af369d193402",
        strip_prefix = "rand_chacha-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.rand_chacha-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_chacha__0_3_0",
        url = "https://crates.io/api/v1/crates/rand_chacha/0.3.0/download",
        type = "tar.gz",
        sha256 = "e12735cf05c9e10bf21534da50a147b924d555dc7a547c42e6bb2d5b6017ae0d",
        strip_prefix = "rand_chacha-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_chacha-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_3_1",
        url = "https://crates.io/api/v1/crates/rand_core/0.3.1/download",
        type = "tar.gz",
        sha256 = "7a6fdeb83b075e8266dcc8762c22776f6877a63111121f5f8c7411e5be7eed4b",
        strip_prefix = "rand_core-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_4_2",
        url = "https://crates.io/api/v1/crates/rand_core/0.4.2/download",
        type = "tar.gz",
        sha256 = "9c33a3c44ca05fa6f1807d8e6743f3824e8509beca625669633be0acbdf509dc",
        strip_prefix = "rand_core-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_5_1",
        url = "https://crates.io/api/v1/crates/rand_core/0.5.1/download",
        type = "tar.gz",
        sha256 = "90bde5296fc891b0cef12a6d03ddccc162ce7b2aff54160af9338f8d40df6d19",
        strip_prefix = "rand_core-0.5.1",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.5.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_6_2",
        url = "https://crates.io/api/v1/crates/rand_core/0.6.2/download",
        type = "tar.gz",
        sha256 = "34cf66eb183df1c5876e2dcf6b13d57340741e8dc255b48e40a26de954d06ae7",
        strip_prefix = "rand_core-0.6.2",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_hc__0_2_0",
        url = "https://crates.io/api/v1/crates/rand_hc/0.2.0/download",
        type = "tar.gz",
        sha256 = "ca3129af7b92a17112d59ad498c6f81eaf463253766b90396d39ea7a39d6613c",
        strip_prefix = "rand_hc-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_hc-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_hc__0_3_0",
        url = "https://crates.io/api/v1/crates/rand_hc/0.3.0/download",
        type = "tar.gz",
        sha256 = "3190ef7066a446f2e7f42e239d161e905420ccab01eb967c9eb27d21b2322a73",
        strip_prefix = "rand_hc-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_hc-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_xorshift__0_2_0",
        url = "https://crates.io/api/v1/crates/rand_xorshift/0.2.0/download",
        type = "tar.gz",
        sha256 = "77d416b86801d23dde1aa643023b775c3a462efc0ed96443add11546cdf1dca8",
        strip_prefix = "rand_xorshift-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rand_xorshift-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rayon__1_5_0",
        url = "https://crates.io/api/v1/crates/rayon/1.5.0/download",
        type = "tar.gz",
        sha256 = "8b0d8e0819fadc20c74ea8373106ead0600e3a67ef1fe8da56e39b9ae7275674",
        strip_prefix = "rayon-1.5.0",
        build_file = Label("//rules/rust/remote:BUILD.rayon-1.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rayon_core__1_9_0",
        url = "https://crates.io/api/v1/crates/rayon-core/1.9.0/download",
        type = "tar.gz",
        sha256 = "9ab346ac5921dc62ffa9f89b7a773907511cdfa5490c572ae9be1be33e8afa4a",
        strip_prefix = "rayon-core-1.9.0",
        build_file = Label("//rules/rust/remote:BUILD.rayon-core-1.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rdrand__0_4_0",
        url = "https://crates.io/api/v1/crates/rdrand/0.4.0/download",
        type = "tar.gz",
        sha256 = "678054eb77286b51581ba43620cc911abf02758c91f93f479767aed0f90458b2",
        strip_prefix = "rdrand-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.rdrand-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_syscall__0_1_57",
        url = "https://crates.io/api/v1/crates/redox_syscall/0.1.57/download",
        type = "tar.gz",
        sha256 = "41cc0f7e4d5d4544e8861606a285bb08d3e70712ccc7d2b84d7c0ccfaf4b05ce",
        strip_prefix = "redox_syscall-0.1.57",
        build_file = Label("//rules/rust/remote:BUILD.redox_syscall-0.1.57.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_syscall__0_2_6",
        url = "https://crates.io/api/v1/crates/redox_syscall/0.2.6/download",
        type = "tar.gz",
        sha256 = "8270314b5ccceb518e7e578952f0b72b88222d02e8f77f5ecf7abbb673539041",
        strip_prefix = "redox_syscall-0.2.6",
        build_file = Label("//rules/rust/remote:BUILD.redox_syscall-0.2.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_users__0_4_0",
        url = "https://crates.io/api/v1/crates/redox_users/0.4.0/download",
        type = "tar.gz",
        sha256 = "528532f3d801c87aec9def2add9ca802fe569e44a544afe633765267840abe64",
        strip_prefix = "redox_users-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.redox_users-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex__1_4_5",
        url = "https://crates.io/api/v1/crates/regex/1.4.5/download",
        type = "tar.gz",
        sha256 = "957056ecddbeba1b26965114e191d2e8589ce74db242b6ea25fc4062427a5c19",
        strip_prefix = "regex-1.4.5",
        build_file = Label("//rules/rust/remote:BUILD.regex-1.4.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_automata__0_1_9",
        url = "https://crates.io/api/v1/crates/regex-automata/0.1.9/download",
        type = "tar.gz",
        sha256 = "ae1ded71d66a4a97f5e961fd0cb25a5f366a42a41570d16a763a69c092c26ae4",
        strip_prefix = "regex-automata-0.1.9",
        build_file = Label("//rules/rust/remote:BUILD.regex-automata-0.1.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_syntax__0_4_2",
        url = "https://crates.io/api/v1/crates/regex-syntax/0.4.2/download",
        type = "tar.gz",
        sha256 = "8e931c58b93d86f080c734bfd2bce7dd0079ae2331235818133c8be7f422e20e",
        strip_prefix = "regex-syntax-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.regex-syntax-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_syntax__0_6_23",
        url = "https://crates.io/api/v1/crates/regex-syntax/0.6.23/download",
        type = "tar.gz",
        sha256 = "24d5f089152e60f62d28b835fbff2cd2e8dc0baf1ac13343bef92ab7eed84548",
        strip_prefix = "regex-syntax-0.6.23",
        build_file = Label("//rules/rust/remote:BUILD.regex-syntax-0.6.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__remove_dir_all__0_5_3",
        url = "https://crates.io/api/v1/crates/remove_dir_all/0.5.3/download",
        type = "tar.gz",
        sha256 = "3acd125665422973a33ac9d3dd2df85edad0f4ae9b00dafb1a05e43a9f5ef8e7",
        strip_prefix = "remove_dir_all-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.remove_dir_all-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__reopen__1_0_2",
        url = "https://crates.io/api/v1/crates/reopen/1.0.2/download",
        type = "tar.gz",
        sha256 = "5edcb3ed00766dec347874689b0a605087dee77a60912f23ce59928756e19631",
        strip_prefix = "reopen-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.reopen-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__resolv_conf__0_7_0",
        url = "https://crates.io/api/v1/crates/resolv-conf/0.7.0/download",
        type = "tar.gz",
        sha256 = "52e44394d2086d010551b14b53b1f24e31647570cd1deb0379e2c21b329aba00",
        strip_prefix = "resolv-conf-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.resolv-conf-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_ini__0_13_0",
        url = "https://crates.io/api/v1/crates/rust-ini/0.13.0/download",
        type = "tar.gz",
        sha256 = "3e52c148ef37f8c375d49d5a73aa70713125b7f19095948a923f80afdeb22ec2",
        strip_prefix = "rust-ini-0.13.0",
        build_file = Label("//rules/rust/remote:BUILD.rust-ini-0.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_stemmers__1_2_0",
        url = "https://crates.io/api/v1/crates/rust-stemmers/1.2.0/download",
        type = "tar.gz",
        sha256 = "e46a2036019fdb888131db7a4c847a1063a7493f971ed94ea82c67eada63ca54",
        strip_prefix = "rust-stemmers-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rust-stemmers-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustc_demangle__0_1_18",
        url = "https://crates.io/api/v1/crates/rustc-demangle/0.1.18/download",
        type = "tar.gz",
        sha256 = "6e3bad0ee36814ca07d7968269dd4b7ec89ec2da10c4bb613928d3077083c232",
        strip_prefix = "rustc-demangle-0.1.18",
        build_file = Label("//rules/rust/remote:BUILD.rustc-demangle-0.1.18.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustc_serialize__0_3_24",
        url = "https://crates.io/api/v1/crates/rustc-serialize/0.3.24/download",
        type = "tar.gz",
        sha256 = "dcf128d1287d2ea9d80910b5f1120d0b8eede3fbf1abe91c40d39ea7d51e6fda",
        strip_prefix = "rustc-serialize-0.3.24",
        build_file = Label("//rules/rust/remote:BUILD.rustc-serialize-0.3.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustc_version__0_2_3",
        url = "https://crates.io/api/v1/crates/rustc_version/0.2.3/download",
        type = "tar.gz",
        sha256 = "138e3e0acb6c9fb258b19b67cb8abd63c00679d2851805ea151465464fe9030a",
        strip_prefix = "rustc_version-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.rustc_version-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rustversion__1_0_4",
        url = "https://crates.io/api/v1/crates/rustversion/1.0.4/download",
        type = "tar.gz",
        sha256 = "cb5d2a036dc6d2d8fd16fde3498b04306e29bd193bf306a57427019b823d5acd",
        strip_prefix = "rustversion-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.rustversion-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rusty_fork__0_3_0",
        url = "https://crates.io/api/v1/crates/rusty-fork/0.3.0/download",
        type = "tar.gz",
        sha256 = "cb3dcc6e454c328bb824492db107ab7c0ae8fcffe4ad210136ef014458c1bc4f",
        strip_prefix = "rusty-fork-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.rusty-fork-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ryu__1_0_5",
        url = "https://crates.io/api/v1/crates/ryu/1.0.5/download",
        type = "tar.gz",
        sha256 = "71d301d4193d031abdd79ff7e3dd721168a9572ef3fe51a1517aba235bd8f86e",
        strip_prefix = "ryu-1.0.5",
        build_file = Label("//rules/rust/remote:BUILD.ryu-1.0.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__safemem__0_3_3",
        url = "https://crates.io/api/v1/crates/safemem/0.3.3/download",
        type = "tar.gz",
        sha256 = "ef703b7cb59335eae2eb93ceb664c0eb7ea6bf567079d843e09420219668e072",
        strip_prefix = "safemem-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.safemem-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__same_file__1_0_6",
        url = "https://crates.io/api/v1/crates/same-file/1.0.6/download",
        type = "tar.gz",
        sha256 = "93fc1dc3aaa9bfed95e02e6eadabb4baf7e3078b0bd1b4d7b6b0b68378900502",
        strip_prefix = "same-file-1.0.6",
        build_file = Label("//rules/rust/remote:BUILD.same-file-1.0.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__scheduled_thread_pool__0_2_5",
        url = "https://crates.io/api/v1/crates/scheduled-thread-pool/0.2.5/download",
        type = "tar.gz",
        sha256 = "dc6f74fd1204073fa02d5d5d68bec8021be4c38690b61264b2fdb48083d0e7d7",
        strip_prefix = "scheduled-thread-pool-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.scheduled-thread-pool-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__scopeguard__1_1_0",
        url = "https://crates.io/api/v1/crates/scopeguard/1.1.0/download",
        type = "tar.gz",
        sha256 = "d29ab0c6d3fc0ee92fe66e2d99f700eab17a8d57d1c1d3b748380fb20baa78cd",
        strip_prefix = "scopeguard-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.scopeguard-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__semver__0_9_0",
        url = "https://crates.io/api/v1/crates/semver/0.9.0/download",
        type = "tar.gz",
        sha256 = "1d7eb9ef2c18661902cc47e535f9bc51b78acd254da71d375c2f6720d9a40403",
        strip_prefix = "semver-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.semver-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__semver_parser__0_7_0",
        url = "https://crates.io/api/v1/crates/semver-parser/0.7.0/download",
        type = "tar.gz",
        sha256 = "388a1df253eca08550bef6c72392cfe7c30914bf41df5269b68cbd6ff8f570a3",
        strip_prefix = "semver-parser-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.semver-parser-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde__0_8_23",
        url = "https://crates.io/api/v1/crates/serde/0.8.23/download",
        type = "tar.gz",
        sha256 = "9dad3f759919b92c3068c696c15c3d17238234498bbdcc80f2c469606f948ac8",
        strip_prefix = "serde-0.8.23",
        build_file = Label("//rules/rust/remote:BUILD.serde-0.8.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde__1_0_125",
        url = "https://crates.io/api/v1/crates/serde/1.0.125/download",
        type = "tar.gz",
        sha256 = "558dc50e1a5a5fa7112ca2ce4effcb321b0300c0d4ccf0776a9f60cd89031171",
        strip_prefix = "serde-1.0.125",
        build_file = Label("//rules/rust/remote:BUILD.serde-1.0.125.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_hjson__0_9_1",
        url = "https://crates.io/api/v1/crates/serde-hjson/0.9.1/download",
        type = "tar.gz",
        sha256 = "6a3a4e0ea8a88553209f6cc6cfe8724ecad22e1acf372793c27d995290fe74f8",
        strip_prefix = "serde-hjson-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.serde-hjson-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_value__0_6_0",
        url = "https://crates.io/api/v1/crates/serde-value/0.6.0/download",
        type = "tar.gz",
        sha256 = "5a65a7291a8a568adcae4c10a677ebcedbc6c9cec91c054dee2ce40b0e3290eb",
        strip_prefix = "serde-value-0.6.0",
        build_file = Label("//rules/rust/remote:BUILD.serde-value-0.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_cbor__0_11_1",
        url = "https://crates.io/api/v1/crates/serde_cbor/0.11.1/download",
        type = "tar.gz",
        sha256 = "1e18acfa2f90e8b735b2836ab8d538de304cbb6729a7360729ea5a895d15a622",
        strip_prefix = "serde_cbor-0.11.1",
        build_file = Label("//rules/rust/remote:BUILD.serde_cbor-0.11.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_derive__1_0_125",
        url = "https://crates.io/api/v1/crates/serde_derive/1.0.125/download",
        type = "tar.gz",
        sha256 = "b093b7a2bb58203b5da3056c05b4ec1fed827dcfdb37347a8841695263b3d06d",
        strip_prefix = "serde_derive-1.0.125",
        build_file = Label("//rules/rust/remote:BUILD.serde_derive-1.0.125.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_json__1_0_64",
        url = "https://crates.io/api/v1/crates/serde_json/1.0.64/download",
        type = "tar.gz",
        sha256 = "799e97dc9fdae36a5c8b8f2cae9ce2ee9fdce2058c57a93e6099d919fd982f79",
        strip_prefix = "serde_json-1.0.64",
        build_file = Label("//rules/rust/remote:BUILD.serde_json-1.0.64.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_qs__0_8_3",
        url = "https://crates.io/api/v1/crates/serde_qs/0.8.3/download",
        type = "tar.gz",
        sha256 = "b22063cd705114614293767c69aa992531f72b0cc8a6b9145801920730fe25e4",
        strip_prefix = "serde_qs-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.serde_qs-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_urlencoded__0_7_0",
        url = "https://crates.io/api/v1/crates/serde_urlencoded/0.7.0/download",
        type = "tar.gz",
        sha256 = "edfa57a7f8d9c1d260a549e7224100f6c43d43f9103e06dd8b4095a9b2b43ce9",
        strip_prefix = "serde_urlencoded-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.serde_urlencoded-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_yaml__0_8_17",
        url = "https://crates.io/api/v1/crates/serde_yaml/0.8.17/download",
        type = "tar.gz",
        sha256 = "15654ed4ab61726bf918a39cb8d98a2e2995b002387807fa6ba58fdf7f59bb23",
        strip_prefix = "serde_yaml-0.8.17",
        build_file = Label("//rules/rust/remote:BUILD.serde_yaml-0.8.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha_1__0_9_4",
        url = "https://crates.io/api/v1/crates/sha-1/0.9.4/download",
        type = "tar.gz",
        sha256 = "dfebf75d25bd900fd1e7d11501efab59bc846dbc76196839663e6637bba9f25f",
        strip_prefix = "sha-1-0.9.4",
        build_file = Label("//rules/rust/remote:BUILD.sha-1-0.9.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha1__0_6_0",
        url = "https://crates.io/api/v1/crates/sha1/0.6.0/download",
        type = "tar.gz",
        sha256 = "2579985fda508104f7587689507983eadd6a6e84dd35d6d115361f530916fa0d",
        strip_prefix = "sha1-0.6.0",
        build_file = Label("//rules/rust/remote:BUILD.sha1-0.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha2__0_9_3",
        url = "https://crates.io/api/v1/crates/sha2/0.9.3/download",
        type = "tar.gz",
        sha256 = "fa827a14b29ab7f44778d14a88d3cb76e949c45083f7dbfa507d0cb699dc12de",
        strip_prefix = "sha2-0.9.3",
        build_file = Label("//rules/rust/remote:BUILD.sha2-0.9.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook__0_2_3",
        url = "https://crates.io/api/v1/crates/signal-hook/0.2.3/download",
        type = "tar.gz",
        sha256 = "844024c8913df6bfbfeee3061075ccc47216a897ac0b54a683dea3dfe16d19af",
        strip_prefix = "signal-hook-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook__0_3_8",
        url = "https://crates.io/api/v1/crates/signal-hook/0.3.8/download",
        type = "tar.gz",
        sha256 = "ef33d6d0cd06e0840fba9985aab098c147e67e05cee14d412d3345ed14ff30ac",
        strip_prefix = "signal-hook-0.3.8",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-0.3.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook_registry__1_3_0",
        url = "https://crates.io/api/v1/crates/signal-hook-registry/1.3.0/download",
        type = "tar.gz",
        sha256 = "16f1d0fef1604ba8f7a073c7e701f213e056707210e9020af4528e0101ce11a6",
        strip_prefix = "signal-hook-registry-1.3.0",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-registry-1.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__siphasher__0_3_5",
        url = "https://crates.io/api/v1/crates/siphasher/0.3.5/download",
        type = "tar.gz",
        sha256 = "cbce6d4507c7e4a3962091436e56e95290cb71fa302d0d270e32130b75fbff27",
        strip_prefix = "siphasher-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.siphasher-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slab__0_4_2",
        url = "https://crates.io/api/v1/crates/slab/0.4.2/download",
        type = "tar.gz",
        sha256 = "c111b5bd5695e56cffe5129854aa230b39c93a305372fdbb2668ca2394eea9f8",
        strip_prefix = "slab-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.slab-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog__2_7_0",
        url = "https://crates.io/api/v1/crates/slog/2.7.0/download",
        type = "tar.gz",
        sha256 = "8347046d4ebd943127157b94d63abb990fcf729dc4e9978927fdf4ac3c998d06",
        strip_prefix = "slog-2.7.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-2.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_async__2_6_0",
        url = "https://crates.io/api/v1/crates/slog-async/2.6.0/download",
        type = "tar.gz",
        sha256 = "c60813879f820c85dbc4eabf3269befe374591289019775898d56a81a804fbdc",
        strip_prefix = "slog-async-2.6.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-async-2.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_json__2_3_0",
        url = "https://crates.io/api/v1/crates/slog-json/2.3.0/download",
        type = "tar.gz",
        sha256 = "ddc0d2aff1f8f325ef660d9a0eb6e6dcd20b30b3f581a5897f58bf42d061c37a",
        strip_prefix = "slog-json-2.3.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-json-2.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_scope__4_4_0",
        url = "https://crates.io/api/v1/crates/slog-scope/4.4.0/download",
        type = "tar.gz",
        sha256 = "2f95a4b4c3274cd2869549da82b57ccc930859bdbf5bcea0424bc5f140b3c786",
        strip_prefix = "slog-scope-4.4.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-scope-4.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_stdlog__4_1_0",
        url = "https://crates.io/api/v1/crates/slog-stdlog/4.1.0/download",
        type = "tar.gz",
        sha256 = "8228ab7302adbf4fcb37e66f3cda78003feb521e7fd9e3847ec117a7784d0f5a",
        strip_prefix = "slog-stdlog-4.1.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-stdlog-4.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_term__2_8_0",
        url = "https://crates.io/api/v1/crates/slog-term/2.8.0/download",
        type = "tar.gz",
        sha256 = "95c1e7e5aab61ced6006149ea772770b84a0d16ce0f7885def313e4829946d76",
        strip_prefix = "slog-term-2.8.0",
        build_file = Label("//rules/rust/remote:BUILD.slog-term-2.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slog_derive__0_2_0",
        url = "https://crates.io/api/v1/crates/slog_derive/0.2.0/download",
        type = "tar.gz",
        sha256 = "a945ec7f7ce853e89ffa36be1e27dce9a43e82ff9093bf3461c30d5da74ed11b",
        strip_prefix = "slog_derive-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.slog_derive-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__smallvec__1_6_1",
        url = "https://crates.io/api/v1/crates/smallvec/1.6.1/download",
        type = "tar.gz",
        sha256 = "fe0f37c9e8f3c5a4a66ad655a93c74daac4ad00c441533bf5c6e7990bb42604e",
        strip_prefix = "smallvec-1.6.1",
        build_file = Label("//rules/rust/remote:BUILD.smallvec-1.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__smawk__0_3_1",
        url = "https://crates.io/api/v1/crates/smawk/0.3.1/download",
        type = "tar.gz",
        sha256 = "f67ad224767faa3c7d8b6d91985b78e70a1324408abcb1cfcc2be4c06bc06043",
        strip_prefix = "smawk-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.smawk-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__snap__1_0_4",
        url = "https://crates.io/api/v1/crates/snap/1.0.4/download",
        type = "tar.gz",
        sha256 = "dc725476a1398f0480d56cd0ad381f6f32acf2642704456f8f59a35df464b59a",
        strip_prefix = "snap-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.snap-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__socket2__0_3_19",
        url = "https://crates.io/api/v1/crates/socket2/0.3.19/download",
        type = "tar.gz",
        sha256 = "122e570113d28d773067fab24266b66753f6ea915758651696b6e35e49f88d6e",
        strip_prefix = "socket2-0.3.19",
        build_file = Label("//rules/rust/remote:BUILD.socket2-0.3.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__socket2__0_4_0",
        url = "https://crates.io/api/v1/crates/socket2/0.4.0/download",
        type = "tar.gz",
        sha256 = "9e3dfc207c526015c632472a77be09cf1b6e46866581aecae5cc38fb4235dea2",
        strip_prefix = "socket2-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.socket2-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stable_deref_trait__1_2_0",
        url = "https://crates.io/api/v1/crates/stable_deref_trait/1.2.0/download",
        type = "tar.gz",
        sha256 = "a8f112729512f8e442d81f95a8a7ddf2b7c6b8a1a6f509a95864142b30cab2d3",
        strip_prefix = "stable_deref_trait-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.stable_deref_trait-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__standback__0_2_17",
        url = "https://crates.io/api/v1/crates/standback/0.2.17/download",
        type = "tar.gz",
        sha256 = "e113fb6f3de07a243d434a56ec6f186dfd51cb08448239fe7bcae73f87ff28ff",
        strip_prefix = "standback-0.2.17",
        build_file = Label("//rules/rust/remote:BUILD.standback-0.2.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__static_assertions__1_1_0",
        url = "https://crates.io/api/v1/crates/static_assertions/1.1.0/download",
        type = "tar.gz",
        sha256 = "a2eb9349b6444b326872e140eb1cf5e7c522154d69e7a0ffb0fb81c06b37543f",
        strip_prefix = "static_assertions-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.static_assertions-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb__0_4_20",
        url = "https://crates.io/api/v1/crates/stdweb/0.4.20/download",
        type = "tar.gz",
        sha256 = "d022496b16281348b52d0e30ae99e01a73d737b2f45d38fed4edf79f9325a1d5",
        strip_prefix = "stdweb-0.4.20",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-0.4.20.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb_derive__0_5_3",
        url = "https://crates.io/api/v1/crates/stdweb-derive/0.5.3/download",
        type = "tar.gz",
        sha256 = "c87a60a40fccc84bef0652345bbbbbe20a605bf5d0ce81719fc476f5c03b50ef",
        strip_prefix = "stdweb-derive-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-derive-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb_internal_macros__0_2_9",
        url = "https://crates.io/api/v1/crates/stdweb-internal-macros/0.2.9/download",
        type = "tar.gz",
        sha256 = "58fa5ff6ad0d98d1ffa8cb115892b6e69d67799f6763e162a1c9db421dc22e11",
        strip_prefix = "stdweb-internal-macros-0.2.9",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-internal-macros-0.2.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stdweb_internal_runtime__0_1_5",
        url = "https://crates.io/api/v1/crates/stdweb-internal-runtime/0.1.5/download",
        type = "tar.gz",
        sha256 = "213701ba3370744dcd1a12960caa4843b3d68b4d1c0a5d575e0d65b2ee9d16c0",
        strip_prefix = "stdweb-internal-runtime-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.stdweb-internal-runtime-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stringprep__0_1_2",
        url = "https://crates.io/api/v1/crates/stringprep/0.1.2/download",
        type = "tar.gz",
        sha256 = "8ee348cb74b87454fff4b551cbf727025810a004f88aeacae7f85b87f4e9a1c1",
        strip_prefix = "stringprep-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.stringprep-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strsim__0_8_0",
        url = "https://crates.io/api/v1/crates/strsim/0.8.0/download",
        type = "tar.gz",
        sha256 = "8ea5119cdb4c55b55d432abb513a0429384878c15dde60cc77b1c99de1a95a6a",
        strip_prefix = "strsim-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.strsim-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strum__0_20_0",
        url = "https://crates.io/api/v1/crates/strum/0.20.0/download",
        type = "tar.gz",
        sha256 = "7318c509b5ba57f18533982607f24070a55d353e90d4cae30c467cdb2ad5ac5c",
        strip_prefix = "strum-0.20.0",
        build_file = Label("//rules/rust/remote:BUILD.strum-0.20.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strum_macros__0_20_1",
        url = "https://crates.io/api/v1/crates/strum_macros/0.20.1/download",
        type = "tar.gz",
        sha256 = "ee8bc6b87a5112aeeab1f4a9f7ab634fe6cbefc4850006df31267f4cfb9e3149",
        strip_prefix = "strum_macros-0.20.1",
        build_file = Label("//rules/rust/remote:BUILD.strum_macros-0.20.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__subtle__2_4_0",
        url = "https://crates.io/api/v1/crates/subtle/2.4.0/download",
        type = "tar.gz",
        sha256 = "1e81da0851ada1f3e9d4312c704aa4f8806f0f9d69faaf8df2f3464b4a9437c2",
        strip_prefix = "subtle-2.4.0",
        build_file = Label("//rules/rust/remote:BUILD.subtle-2.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__syn__1_0_69",
        url = "https://crates.io/api/v1/crates/syn/1.0.69/download",
        type = "tar.gz",
        sha256 = "48fe99c6bd8b1cc636890bcc071842de909d902c81ac7dab53ba33c421ab8ffb",
        strip_prefix = "syn-1.0.69",
        build_file = Label("//rules/rust/remote:BUILD.syn-1.0.69.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__synstructure__0_12_4",
        url = "https://crates.io/api/v1/crates/synstructure/0.12.4/download",
        type = "tar.gz",
        sha256 = "b834f2d66f734cb897113e34aaff2f1ab4719ca946f9a7358dba8f8064148701",
        strip_prefix = "synstructure-0.12.4",
        build_file = Label("//rules/rust/remote:BUILD.synstructure-0.12.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__take_mut__0_2_2",
        url = "https://crates.io/api/v1/crates/take_mut/0.2.2/download",
        type = "tar.gz",
        sha256 = "f764005d11ee5f36500a149ace24e00e3da98b0158b3e2d53a7495660d3f4d60",
        strip_prefix = "take_mut-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.take_mut-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_fst__0_3_0",
        url = "https://crates.io/api/v1/crates/tantivy-fst/0.3.0/download",
        type = "tar.gz",
        sha256 = "cb20cdc0d83e9184560bdde9cd60142dbb4af2e0f770e88fce45770495224205",
        strip_prefix = "tantivy-fst-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-fst-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tar__0_4_33",
        url = "https://crates.io/api/v1/crates/tar/0.4.33/download",
        type = "tar.gz",
        sha256 = "c0bcfbd6a598361fda270d82469fff3d65089dc33e175c9a131f7b4cd395f228",
        strip_prefix = "tar-0.4.33",
        build_file = Label("//rules/rust/remote:BUILD.tar-0.4.33.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tempdir__0_3_7",
        url = "https://crates.io/api/v1/crates/tempdir/0.3.7/download",
        type = "tar.gz",
        sha256 = "15f2b5fb00ccdf689e0149d1b1b3c03fead81c2b37735d812fa8bddbbf41b6d8",
        strip_prefix = "tempdir-0.3.7",
        build_file = Label("//rules/rust/remote:BUILD.tempdir-0.3.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tempfile__3_2_0",
        url = "https://crates.io/api/v1/crates/tempfile/3.2.0/download",
        type = "tar.gz",
        sha256 = "dac1c663cfc93810f88aed9b8941d48cabf856a1b111c29a40439018d870eb22",
        strip_prefix = "tempfile-3.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tempfile-3.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__term__0_7_0",
        url = "https://crates.io/api/v1/crates/term/0.7.0/download",
        type = "tar.gz",
        sha256 = "c59df8ac95d96ff9bede18eb7300b0fda5e5d8d90960e76f8e14ae765eedbf1f",
        strip_prefix = "term-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.term-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__termcolor__1_1_2",
        url = "https://crates.io/api/v1/crates/termcolor/1.1.2/download",
        type = "tar.gz",
        sha256 = "2dfed899f0eb03f32ee8c6a0aabdb8a7949659e3466561fc0adf54e26d88c5f4",
        strip_prefix = "termcolor-1.1.2",
        build_file = Label("//rules/rust/remote:BUILD.termcolor-1.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__textwrap__0_11_0",
        url = "https://crates.io/api/v1/crates/textwrap/0.11.0/download",
        type = "tar.gz",
        sha256 = "d326610f408c7a4eb6f51c37c330e496b08506c9457c9d34287ecc38809fb060",
        strip_prefix = "textwrap-0.11.0",
        build_file = Label("//rules/rust/remote:BUILD.textwrap-0.11.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__textwrap__0_13_4",
        url = "https://crates.io/api/v1/crates/textwrap/0.13.4/download",
        type = "tar.gz",
        sha256 = "cd05616119e612a8041ef58f2b578906cc2531a6069047ae092cfb86a325d835",
        strip_prefix = "textwrap-0.13.4",
        build_file = Label("//rules/rust/remote:BUILD.textwrap-0.13.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thiserror__1_0_24",
        url = "https://crates.io/api/v1/crates/thiserror/1.0.24/download",
        type = "tar.gz",
        sha256 = "e0f4a65597094d4483ddaed134f409b2cb7c1beccf25201a9f73c719254fa98e",
        strip_prefix = "thiserror-1.0.24",
        build_file = Label("//rules/rust/remote:BUILD.thiserror-1.0.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thiserror_impl__1_0_24",
        url = "https://crates.io/api/v1/crates/thiserror-impl/1.0.24/download",
        type = "tar.gz",
        sha256 = "7765189610d8241a44529806d6fd1f2e0a08734313a35d5b3a556f92b381f3c0",
        strip_prefix = "thiserror-impl-1.0.24",
        build_file = Label("//rules/rust/remote:BUILD.thiserror-impl-1.0.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thread_id__3_3_0",
        url = "https://crates.io/api/v1/crates/thread-id/3.3.0/download",
        type = "tar.gz",
        sha256 = "c7fbf4c9d56b320106cd64fd024dadfa0be7cb4706725fc44a7d7ce952d820c1",
        strip_prefix = "thread-id-3.3.0",
        build_file = Label("//rules/rust/remote:BUILD.thread-id-3.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thread_local__1_1_3",
        url = "https://crates.io/api/v1/crates/thread_local/1.1.3/download",
        type = "tar.gz",
        sha256 = "8018d24e04c95ac8790716a5987d0fec4f8b27249ffa0f7d33f1369bdfb88cbd",
        strip_prefix = "thread_local-1.1.3",
        build_file = Label("//rules/rust/remote:BUILD.thread_local-1.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__threadpool__1_8_1",
        url = "https://crates.io/api/v1/crates/threadpool/1.8.1/download",
        type = "tar.gz",
        sha256 = "d050e60b33d41c19108b32cea32164033a9013fe3b46cbd4457559bfbf77afaa",
        strip_prefix = "threadpool-1.8.1",
        build_file = Label("//rules/rust/remote:BUILD.threadpool-1.8.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time__0_1_43",
        url = "https://crates.io/api/v1/crates/time/0.1.43/download",
        type = "tar.gz",
        sha256 = "ca8a50ef2360fbd1eeb0ecd46795a87a19024eb4b53c5dc916ca1fd95fe62438",
        strip_prefix = "time-0.1.43",
        build_file = Label("//rules/rust/remote:BUILD.time-0.1.43.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time__0_2_26",
        url = "https://crates.io/api/v1/crates/time/0.2.26/download",
        type = "tar.gz",
        sha256 = "08a8cbfbf47955132d0202d1662f49b2423ae35862aee471f3ba4b133358f372",
        strip_prefix = "time-0.2.26",
        build_file = Label("//rules/rust/remote:BUILD.time-0.2.26.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time_macros__0_1_1",
        url = "https://crates.io/api/v1/crates/time-macros/0.1.1/download",
        type = "tar.gz",
        sha256 = "957e9c6e26f12cb6d0dd7fc776bb67a706312e7299aed74c8dd5b17ebb27e2f1",
        strip_prefix = "time-macros-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.time-macros-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time_macros_impl__0_1_1",
        url = "https://crates.io/api/v1/crates/time-macros-impl/0.1.1/download",
        type = "tar.gz",
        sha256 = "e5c3be1edfad6027c69f5491cf4cb310d1a71ecd6af742788c6ff8bced86b8fa",
        strip_prefix = "time-macros-impl-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.time-macros-impl-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tinytemplate__1_2_1",
        url = "https://crates.io/api/v1/crates/tinytemplate/1.2.1/download",
        type = "tar.gz",
        sha256 = "be4d6b5f19ff7664e8c98d03e2139cb510db9b0a60b55f8e8709b689d939b6bc",
        strip_prefix = "tinytemplate-1.2.1",
        build_file = Label("//rules/rust/remote:BUILD.tinytemplate-1.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tinyvec__1_2_0",
        url = "https://crates.io/api/v1/crates/tinyvec/1.2.0/download",
        type = "tar.gz",
        sha256 = "5b5220f05bb7de7f3f53c7c065e1199b3172696fe2db9f9c4d8ad9b4ee74c342",
        strip_prefix = "tinyvec-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tinyvec-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tinyvec_macros__0_1_0",
        url = "https://crates.io/api/v1/crates/tinyvec_macros/0.1.0/download",
        type = "tar.gz",
        sha256 = "cda74da7e1a664f795bb1f8a87ec406fb89a02522cf6e50620d016add6dbbf5c",
        strip_prefix = "tinyvec_macros-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.tinyvec_macros-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tls_api__0_4_0",
        url = "https://crates.io/api/v1/crates/tls-api/0.4.0/download",
        type = "tar.gz",
        sha256 = "4ebb4107c167a4087349fcf08aea4debc358fe69d60fe1df991781842cfe98a3",
        strip_prefix = "tls-api-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.tls-api-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tls_api_stub__0_4_0",
        url = "https://crates.io/api/v1/crates/tls-api-stub/0.4.0/download",
        type = "tar.gz",
        sha256 = "6f8ff269def04f25ae84b9aac156a400b92c97018a184036548c91cedaafd783",
        strip_prefix = "tls-api-stub-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.tls-api-stub-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio__0_2_25",
        url = "https://crates.io/api/v1/crates/tokio/0.2.25/download",
        type = "tar.gz",
        sha256 = "6703a273949a90131b290be1fe7b039d0fc884aa1935860dfcbe056f28cd8092",
        strip_prefix = "tokio-0.2.25",
        build_file = Label("//rules/rust/remote:BUILD.tokio-0.2.25.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio__1_5_0",
        url = "https://crates.io/api/v1/crates/tokio/1.5.0/download",
        type = "tar.gz",
        sha256 = "83f0c8e7c0addab50b663055baf787d0af7f413a46e6e7fb9559a4e4db7137a5",
        strip_prefix = "tokio-1.5.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-1.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_macros__0_2_6",
        url = "https://crates.io/api/v1/crates/tokio-macros/0.2.6/download",
        type = "tar.gz",
        sha256 = "e44da00bfc73a25f814cd8d7e57a68a5c31b74b3152a0a1d1f590c97ed06265a",
        strip_prefix = "tokio-macros-0.2.6",
        build_file = Label("//rules/rust/remote:BUILD.tokio-macros-0.2.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_pg_mapper__0_2_0",
        url = "https://crates.io/api/v1/crates/tokio-pg-mapper/0.2.0/download",
        type = "tar.gz",
        sha256 = "93f2b78f3566383ffabc553c72bbb2f129962a54886c5c4d8e8c706f84eceab8",
        strip_prefix = "tokio-pg-mapper-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-pg-mapper-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_pg_mapper_derive__0_2_0",
        url = "https://crates.io/api/v1/crates/tokio-pg-mapper-derive/0.2.0/download",
        type = "tar.gz",
        sha256 = "8548f756cd6eb4069c5af0fb0cec57001fb42bd1fb7330d8f24067ee3fa62608",
        strip_prefix = "tokio-pg-mapper-derive-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-pg-mapper-derive-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_postgres__0_5_5",
        url = "https://crates.io/api/v1/crates/tokio-postgres/0.5.5/download",
        type = "tar.gz",
        sha256 = "55a2482c9fe4dd481723cf5c0616f34afc710e55dcda0944e12e7b3316117892",
        strip_prefix = "tokio-postgres-0.5.5",
        build_file = Label("//rules/rust/remote:BUILD.tokio-postgres-0.5.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_postgres__0_7_1",
        url = "https://crates.io/api/v1/crates/tokio-postgres/0.7.1/download",
        type = "tar.gz",
        sha256 = "98779a950cb6ef76f8ad71c411176115c5c1200a83eeeca4dd9f61e3fc4836c8",
        strip_prefix = "tokio-postgres-0.7.1",
        build_file = Label("//rules/rust/remote:BUILD.tokio-postgres-0.7.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_2_0",
        url = "https://crates.io/api/v1/crates/tokio-util/0.2.0/download",
        type = "tar.gz",
        sha256 = "571da51182ec208780505a32528fc5512a8fe1443ab960b3f2f3ef093cd16930",
        strip_prefix = "tokio-util-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_3_1",
        url = "https://crates.io/api/v1/crates/tokio-util/0.3.1/download",
        type = "tar.gz",
        sha256 = "be8242891f2b6cbef26a2d7e8605133c2c554cd35b3e4948ea892d6d68436499",
        strip_prefix = "tokio-util-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_6_6",
        url = "https://crates.io/api/v1/crates/tokio-util/0.6.6/download",
        type = "tar.gz",
        sha256 = "940a12c99365c31ea8dd9ba04ec1be183ffe4920102bb7122c2f515437601e8e",
        strip_prefix = "tokio-util-0.6.6",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.6.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__toml__0_5_8",
        url = "https://crates.io/api/v1/crates/toml/0.5.8/download",
        type = "tar.gz",
        sha256 = "a31142970826733df8241ef35dc040ef98c679ab14d7c3e54d827099b3acecaa",
        strip_prefix = "toml-0.5.8",
        build_file = Label("//rules/rust/remote:BUILD.toml-0.5.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing__0_1_25",
        url = "https://crates.io/api/v1/crates/tracing/0.1.25/download",
        type = "tar.gz",
        sha256 = "01ebdc2bb4498ab1ab5f5b73c5803825e60199229ccba0698170e3be0e7f959f",
        strip_prefix = "tracing-0.1.25",
        build_file = Label("//rules/rust/remote:BUILD.tracing-0.1.25.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_core__0_1_17",
        url = "https://crates.io/api/v1/crates/tracing-core/0.1.17/download",
        type = "tar.gz",
        sha256 = "f50de3927f93d202783f4513cda820ab47ef17f624b03c096e86ef00c67e6b5f",
        strip_prefix = "tracing-core-0.1.17",
        build_file = Label("//rules/rust/remote:BUILD.tracing-core-0.1.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_futures__0_2_5",
        url = "https://crates.io/api/v1/crates/tracing-futures/0.2.5/download",
        type = "tar.gz",
        sha256 = "97d095ae15e245a057c8e8451bab9b3ee1e1f68e9ba2b4fbc18d0ac5237835f2",
        strip_prefix = "tracing-futures-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.tracing-futures-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__traitobject__0_1_0",
        url = "https://crates.io/api/v1/crates/traitobject/0.1.0/download",
        type = "tar.gz",
        sha256 = "efd1f82c56340fdf16f2a953d7bda4f8fdffba13d93b00844c25572110b26079",
        strip_prefix = "traitobject-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.traitobject-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__trust_dns_proto__0_19_7",
        url = "https://crates.io/api/v1/crates/trust-dns-proto/0.19.7/download",
        type = "tar.gz",
        sha256 = "1cad71a0c0d68ab9941d2fb6e82f8fb2e86d9945b94e1661dd0aaea2b88215a9",
        strip_prefix = "trust-dns-proto-0.19.7",
        build_file = Label("//rules/rust/remote:BUILD.trust-dns-proto-0.19.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__trust_dns_resolver__0_19_7",
        url = "https://crates.io/api/v1/crates/trust-dns-resolver/0.19.7/download",
        type = "tar.gz",
        sha256 = "710f593b371175db53a26d0b38ed2978fafb9e9e8d3868b1acd753ea18df0ceb",
        strip_prefix = "trust-dns-resolver-0.19.7",
        build_file = Label("//rules/rust/remote:BUILD.trust-dns-resolver-0.19.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__typemap__0_3_3",
        url = "https://crates.io/api/v1/crates/typemap/0.3.3/download",
        type = "tar.gz",
        sha256 = "653be63c80a3296da5551e1bfd2cca35227e13cdd08c6668903ae2f4f77aa1f6",
        strip_prefix = "typemap-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.typemap-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__typenum__1_13_0",
        url = "https://crates.io/api/v1/crates/typenum/1.13.0/download",
        type = "tar.gz",
        sha256 = "879f6906492a7cd215bfa4cf595b600146ccfac0c79bcbd1f3000162af5e8b06",
        strip_prefix = "typenum-1.13.0",
        build_file = Label("//rules/rust/remote:BUILD.typenum-1.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_bidi__0_3_5",
        url = "https://crates.io/api/v1/crates/unicode-bidi/0.3.5/download",
        type = "tar.gz",
        sha256 = "eeb8be209bb1c96b7c177c7420d26e04eccacb0eeae6b980e35fcb74678107e0",
        strip_prefix = "unicode-bidi-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.unicode-bidi-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_normalization__0_1_17",
        url = "https://crates.io/api/v1/crates/unicode-normalization/0.1.17/download",
        type = "tar.gz",
        sha256 = "07fbfce1c8a97d547e8b5334978438d9d6ec8c20e38f56d4a4374d181493eaef",
        strip_prefix = "unicode-normalization-0.1.17",
        build_file = Label("//rules/rust/remote:BUILD.unicode-normalization-0.1.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_segmentation__1_7_1",
        url = "https://crates.io/api/v1/crates/unicode-segmentation/1.7.1/download",
        type = "tar.gz",
        sha256 = "bb0d2e7be6ae3a5fa87eed5fb451aff96f2573d2694942e40543ae0bbe19c796",
        strip_prefix = "unicode-segmentation-1.7.1",
        build_file = Label("//rules/rust/remote:BUILD.unicode-segmentation-1.7.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_width__0_1_8",
        url = "https://crates.io/api/v1/crates/unicode-width/0.1.8/download",
        type = "tar.gz",
        sha256 = "9337591893a19b88d8d87f2cec1e73fad5cdfd10e5a6f349f498ad6ea2ffb1e3",
        strip_prefix = "unicode-width-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.unicode-width-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_xid__0_2_1",
        url = "https://crates.io/api/v1/crates/unicode-xid/0.2.1/download",
        type = "tar.gz",
        sha256 = "f7fe0bb3479651439c9112f72b6c505038574c9fbb575ed1bf3b797fa39dd564",
        strip_prefix = "unicode-xid-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.unicode-xid-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unix_socket__0_5_0",
        url = "https://crates.io/api/v1/crates/unix_socket/0.5.0/download",
        type = "tar.gz",
        sha256 = "6aa2700417c405c38f5e6902d699345241c28c0b7ade4abaad71e35a87eb1564",
        strip_prefix = "unix_socket-0.5.0",
        build_file = Label("//rules/rust/remote:BUILD.unix_socket-0.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unsafe_any__0_4_2",
        url = "https://crates.io/api/v1/crates/unsafe-any/0.4.2/download",
        type = "tar.gz",
        sha256 = "f30360d7979f5e9c6e6cea48af192ea8fab4afb3cf72597154b8f08935bc9c7f",
        strip_prefix = "unsafe-any-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.unsafe-any-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__url__2_2_1",
        url = "https://crates.io/api/v1/crates/url/2.2.1/download",
        type = "tar.gz",
        sha256 = "9ccd964113622c8e9322cfac19eb1004a07e636c545f325da085d5cdde6f1f8b",
        strip_prefix = "url-2.2.1",
        build_file = Label("//rules/rust/remote:BUILD.url-2.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__urlparse__0_7_3",
        url = "https://crates.io/api/v1/crates/urlparse/0.7.3/download",
        type = "tar.gz",
        sha256 = "110352d4e9076c67839003c7788d8604e24dcded13e0b375af3efaa8cf468517",
        strip_prefix = "urlparse-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.urlparse-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__utf8_ranges__1_0_4",
        url = "https://crates.io/api/v1/crates/utf8-ranges/1.0.4/download",
        type = "tar.gz",
        sha256 = "b4ae116fef2b7fea257ed6440d3cfcff7f190865f170cdad00bb6465bf18ecba",
        strip_prefix = "utf8-ranges-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.utf8-ranges-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__uuid__0_8_2",
        url = "https://crates.io/api/v1/crates/uuid/0.8.2/download",
        type = "tar.gz",
        sha256 = "bc5cf98d8186244414c848017f0e2676b3fcb46807f6668a97dfe67359a3c4b7",
        strip_prefix = "uuid-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.uuid-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__vec_map__0_8_2",
        url = "https://crates.io/api/v1/crates/vec_map/0.8.2/download",
        type = "tar.gz",
        sha256 = "f1bddf1187be692e79c5ffeab891132dfb0f236ed36a43c7ed39f1165ee20191",
        strip_prefix = "vec_map-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.vec_map-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__version_check__0_9_3",
        url = "https://crates.io/api/v1/crates/version_check/0.9.3/download",
        type = "tar.gz",
        sha256 = "5fecdca9a5291cc2b8dcf7dc02453fee791a280f3743cb0905f8822ae463b3fe",
        strip_prefix = "version_check-0.9.3",
        build_file = Label("//rules/rust/remote:BUILD.version_check-0.9.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__void__1_0_2",
        url = "https://crates.io/api/v1/crates/void/1.0.2/download",
        type = "tar.gz",
        sha256 = "6a02e4885ed3bc0f2de90ea6dd45ebcbb66dacffe03547fadbb0eeae2770887d",
        strip_prefix = "void-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.void-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wait_timeout__0_2_0",
        url = "https://crates.io/api/v1/crates/wait-timeout/0.2.0/download",
        type = "tar.gz",
        sha256 = "9f200f5b12eb75f8c1ed65abd4b2db8a6e1b138a20de009dacee265a2498f3f6",
        strip_prefix = "wait-timeout-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.wait-timeout-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__walkdir__2_3_2",
        url = "https://crates.io/api/v1/crates/walkdir/2.3.2/download",
        type = "tar.gz",
        sha256 = "808cf2735cd4b6866113f648b791c6adc5714537bc222d9347bb203386ffda56",
        strip_prefix = "walkdir-2.3.2",
        build_file = Label("//rules/rust/remote:BUILD.walkdir-2.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasi__0_10_2_wasi_snapshot_preview1",
        url = "https://crates.io/api/v1/crates/wasi/0.10.2+wasi-snapshot-preview1/download",
        type = "tar.gz",
        sha256 = "fd6fbd9a79829dd1ad0cc20627bf1ed606756a7f77edff7b66b7064f9cb327c6",
        strip_prefix = "wasi-0.10.2+wasi-snapshot-preview1",
        build_file = Label("//rules/rust/remote:BUILD.wasi-0.10.2+wasi-snapshot-preview1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasi__0_9_0_wasi_snapshot_preview1",
        url = "https://crates.io/api/v1/crates/wasi/0.9.0+wasi-snapshot-preview1/download",
        type = "tar.gz",
        sha256 = "cccddf32554fecc6acb585f82a32a72e28b48f8c4c1883ddfeeeaa96f7d8e519",
        strip_prefix = "wasi-0.9.0+wasi-snapshot-preview1",
        build_file = Label("//rules/rust/remote:BUILD.wasi-0.9.0+wasi-snapshot-preview1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen__0_2_73",
        url = "https://crates.io/api/v1/crates/wasm-bindgen/0.2.73/download",
        type = "tar.gz",
        sha256 = "83240549659d187488f91f33c0f8547cbfef0b2088bc470c116d1d260ef623d9",
        strip_prefix = "wasm-bindgen-0.2.73",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-0.2.73.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_backend__0_2_73",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-backend/0.2.73/download",
        type = "tar.gz",
        sha256 = "ae70622411ca953215ca6d06d3ebeb1e915f0f6613e3b495122878d7ebec7dae",
        strip_prefix = "wasm-bindgen-backend-0.2.73",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-backend-0.2.73.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_macro__0_2_73",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-macro/0.2.73/download",
        type = "tar.gz",
        sha256 = "3e734d91443f177bfdb41969de821e15c516931c3c3db3d318fa1b68975d0f6f",
        strip_prefix = "wasm-bindgen-macro-0.2.73",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-macro-0.2.73.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_macro_support__0_2_73",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-macro-support/0.2.73/download",
        type = "tar.gz",
        sha256 = "d53739ff08c8a68b0fdbcd54c372b8ab800b1449ab3c9d706503bc7dd1621b2c",
        strip_prefix = "wasm-bindgen-macro-support-0.2.73",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-macro-support-0.2.73.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_shared__0_2_73",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-shared/0.2.73/download",
        type = "tar.gz",
        sha256 = "d9a543ae66aa233d14bb765ed9af4a33e81b8b58d1584cf1b47ff8cd0b9e4489",
        strip_prefix = "wasm-bindgen-shared-0.2.73",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-shared-0.2.73.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__web_sys__0_3_50",
        url = "https://crates.io/api/v1/crates/web-sys/0.3.50/download",
        type = "tar.gz",
        sha256 = "a905d57e488fec8861446d3393670fb50d27a262344013181c2cdf9fff5481be",
        strip_prefix = "web-sys-0.3.50",
        build_file = Label("//rules/rust/remote:BUILD.web-sys-0.3.50.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__widestring__0_4_3",
        url = "https://crates.io/api/v1/crates/widestring/0.4.3/download",
        type = "tar.gz",
        sha256 = "c168940144dd21fd8046987c16a46a33d5fc84eec29ef9dcddc2ac9e31526b7c",
        strip_prefix = "widestring-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.widestring-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi__0_2_8",
        url = "https://crates.io/api/v1/crates/winapi/0.2.8/download",
        type = "tar.gz",
        sha256 = "167dc9d6949a9b857f3451275e911c3f44255842c1f7a76f33c55103a909087a",
        strip_prefix = "winapi-0.2.8",
        build_file = Label("//rules/rust/remote:BUILD.winapi-0.2.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi__0_3_9",
        url = "https://crates.io/api/v1/crates/winapi/0.3.9/download",
        type = "tar.gz",
        sha256 = "5c839a674fcd7a98952e593242ea400abe93992746761e38641405d28b00f419",
        strip_prefix = "winapi-0.3.9",
        build_file = Label("//rules/rust/remote:BUILD.winapi-0.3.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_build__0_1_1",
        url = "https://crates.io/api/v1/crates/winapi-build/0.1.1/download",
        type = "tar.gz",
        sha256 = "2d315eee3b34aca4797b2da6b13ed88266e6d612562a0c46390af8299fc699bc",
        strip_prefix = "winapi-build-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.winapi-build-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_i686_pc_windows_gnu__0_4_0",
        url = "https://crates.io/api/v1/crates/winapi-i686-pc-windows-gnu/0.4.0/download",
        type = "tar.gz",
        sha256 = "ac3b87c63620426dd9b991e5ce0329eff545bccbbb34f3be09ff6fb6ab51b7b6",
        strip_prefix = "winapi-i686-pc-windows-gnu-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.winapi-i686-pc-windows-gnu-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_util__0_1_5",
        url = "https://crates.io/api/v1/crates/winapi-util/0.1.5/download",
        type = "tar.gz",
        sha256 = "70ec6ce85bb158151cae5e5c87f95a8e97d2c0c4b001223f33a334e3ce5de178",
        strip_prefix = "winapi-util-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.winapi-util-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_x86_64_pc_windows_gnu__0_4_0",
        url = "https://crates.io/api/v1/crates/winapi-x86_64-pc-windows-gnu/0.4.0/download",
        type = "tar.gz",
        sha256 = "712e227841d057c1ee1cd2fb22fa7e5a5461ae8e48fa2ca79ec42cfc1931183f",
        strip_prefix = "winapi-x86_64-pc-windows-gnu-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.winapi-x86_64-pc-windows-gnu-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winreg__0_6_2",
        url = "https://crates.io/api/v1/crates/winreg/0.6.2/download",
        type = "tar.gz",
        sha256 = "b2986deb581c4fe11b621998a5e53361efe6b48a151178d0cd9eeffa4dc6acc9",
        strip_prefix = "winreg-0.6.2",
        build_file = Label("//rules/rust/remote:BUILD.winreg-0.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ws2_32_sys__0_2_1",
        url = "https://crates.io/api/v1/crates/ws2_32-sys/0.2.1/download",
        type = "tar.gz",
        sha256 = "d59cefebd0c892fa2dd6de581e937301d8552cb44489cdff035c6187cb63fa5e",
        strip_prefix = "ws2_32-sys-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.ws2_32-sys-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__xattr__0_2_2",
        url = "https://crates.io/api/v1/crates/xattr/0.2.2/download",
        type = "tar.gz",
        sha256 = "244c3741f4240ef46274860397c7c74e50eb23624996930e484c16679633a54c",
        strip_prefix = "xattr-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.xattr-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__yaml_rust__0_4_5",
        url = "https://crates.io/api/v1/crates/yaml-rust/0.4.5/download",
        type = "tar.gz",
        sha256 = "56c1936c4cc7a1c9ab21a1ebb602eb942ba868cbd44a99cb7cdc5892335e1c85",
        strip_prefix = "yaml-rust-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.yaml-rust-0.4.5.bazel"),
    )
