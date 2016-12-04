package com.smallspider.mapper;

/**
 * Created by yangyang on 2016/12/4.
 */
public interface Mapper<T> {
    int add(T t);
    int update(T t);
    int delete(T t);
    T get(T t);
}
