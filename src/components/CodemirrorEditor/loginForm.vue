<template>
    <el-dialog
        title="登录"
        class="login__dialog"
        :visible="value"
        @close="$emit('closelogin')">

        <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">
            <h3 class="login-title">欢迎登录</h3>
            <el-form-item label="账号"  prop="username">
                <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit('loginForm')">登录</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>

import axios from "axios";
import { MessageBox, Message } from "element-ui";  // 引入

export default {
    props: {
        value: {
            type: Boolean,
            default: false,
        },
        rules: {
          username: [
            {required: true, message: '账号不可为空', trigger: 'blur'}
          ],

          password: [
            {required: true, message: '密码不可为空', trigger: 'blur'}
          ]
        },
    },

    data() {
        return {
            form:{
                username:"",
                password:"",
            }, 
        }
    },
    methods: {
      onSubmit(formName) {
        const self = this;
        // 为表单绑定验证功能
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // 使用 vue-router 路由到指定页面，该方式称之为编程式导航
            // this.$router.push("/main");
            // console.log(this.form.username);
            // console.log(this.form.password);

            axios.post("http://127.0.0.1:8000/api/login/", {
                username: this.form.username,
                password: this.form.password,
            })
            .then(function (res) {
                if(res.data.login == "true") {
                    Message({
                        type: "success",
                        message: "登录成功",
                        showClose: true,
                    });

                    localStorage.setItem("Flag", "isLogin");
                     self.$emit('closelogin');
                     self.$emit('refresh');
                } else {
                    MessageBox.alert(
                        "账号或密码错误",
                        "提示",
                        { type: "warning" }
                    );
                }
            })
            .catch(function (error) {
                console.log(error);
            });

          } else {
            this.dialogVisible = true;
            return false;
          }
        });
      }
    }
}

</script>

<style lang="scss" scoped>
    // .login__dialog{

    // }
    .el-form-item {
        margin-bottom: 22px !important;
    }
  .login-box {
    border: 1px solid #DCDFE6;
    width: 50%;
    margin: 10% auto;
    padding: 35px 35px 15px 35px;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    box-shadow: 0 0 25px #909399;
  }

  .login-title {
    text-align: center;
    margin: 0 auto 40px auto;
    color: #303133;
  }
</style>
