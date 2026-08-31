package com.nexus.metadata;

public interface MetadataRepository {
    void saveWithVersionCheck(MetadataResult result, long expectedVersion);
}
