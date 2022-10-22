import { Promise, reject } from "q";
import fileApi from "../../api/fetcharticle";

export function getArticleList(token) {
    return new Promise((resolve, reject) => {
        fileApi.getArticleList(token)
            .then((res) => {
                resolve(res);
            })
            .catch((err) => {
                reject(err);
            });
    });
}