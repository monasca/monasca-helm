CREATE DATABASE IF NOT EXISTS `monasca_transform` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `monasca_transform`;

SET foreign_key_checks = 0;

CREATE TABLE IF NOT EXISTS `kafka_offsets` (
  `id` INTEGER AUTO_INCREMENT NOT NULL,
  `topic` varchar(128) NOT NULL,
  `until_offset` BIGINT NULL,
  `from_offset` BIGINT NULL,
  `app_name` varchar(128) NOT NULL,
  `partition` integer NOT NULL,
  `batch_time` varchar(20) NOT NULL,
  `last_updated` varchar(20) NOT NULL,
  `revision` integer NOT NULL,
  PRIMARY KEY (`id`, `app_name`, `topic`, `partition`, `revision`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS `transform_specs` (
  `metric_id` varchar(128) NOT NULL,
  `transform_spec` varchar(2048) NOT NULL,
  PRIMARY KEY (`metric_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `pre_transform_specs` (
  `event_type` varchar(128) NOT NULL,
  `pre_transform_spec` varchar(2048) NOT NULL,
  PRIMARY KEY (`event_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

GRANT ALL ON monasca_transform.* TO 'm-transform'@'%' IDENTIFIED BY 'password';

GRANT ALL ON monasca_transform.* TO 'm-transform'@'localhost' IDENTIFIED BY 'password';
