import { json } from "body-parser";
import fetch from "./fetch";

const base_url = "http://127.0.0.1:8000"

async function getArticleList(token) {
    const res = await fetch({
        url: base_url + "/api/articlelist",
        method: "get",
        data: {
            "m": "list",
            token: token,
        },
    });

    return res;

    // return '{"data":[{"id":0, "title":"第一篇文章"},{"id":1,"title":"第一篇文章"}]}';

}

export default {
    getArticleList,
};