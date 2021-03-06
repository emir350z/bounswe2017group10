package com.bounswe2017.group10.atlas.httpbody;

import com.bounswe2017.group10.atlas.adapter.CommentRow;
import com.bounswe2017.group10.atlas.util.Utils;
import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.io.Serializable;

/**
 * Created by mutas on 21.11.2017.
 */




public class Comment implements Serializable {



    private class UserInfo implements Serializable {

        @SerializedName("username")
        @Expose
        private String username;

        @SerializedName("picture")
        @Expose
        private String picture;

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getPicture() {
            return picture;
        }

        public void setPicture(String picture) {
            this.picture = picture;
        }
    }

    @SerializedName("user_info")
    @Expose
    private UserInfo userInfo;

    @SerializedName("user")
    @Expose
    private String user;

    @SerializedName("text")
    @Expose
    private String text;

    @SerializedName("created_time")
    @Expose
    private String createTime;

    @SerializedName("updated_time")
    @Expose
    private String updateTime;

    @SerializedName("cultural_heritage_item")
    @Expose
    private String itemKey;

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getCreateTime() {
        return createTime;
    }

    public void setCreateTime(String createTime) {
        this.createTime = createTime;
    }

    public String getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(String updateTime) {
        this.updateTime = updateTime;
    }

    public String getItemKey() {
        return itemKey;
    }

    public void setItemKey(String itemKey) {
        this.itemKey = itemKey;
    }

    public CommentRow toCommentRow() {
        return new CommentRow(this.getUserInfo().getUsername(), this.getCreateTime(), this.getText(), this.getUserInfo().getPicture());
    }

    public UserInfo getUserInfo() {
        return userInfo;
    }

    public void setUserInfo(UserInfo userInfo) {
        this.userInfo = userInfo;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Comment)) {
            return false;
        }
        Comment other = (Comment)obj;
        // all fields must be equal
        return Utils.objectEquals(this.user, other.user) &&
                Utils.objectEquals(this.text, other.text) &&
                Utils.objectEquals(this.createTime, other.createTime) &&
                Utils.objectEquals(this.updateTime, other.updateTime) &&
                Utils.objectEquals(this.itemKey, other.itemKey);
    }
}


